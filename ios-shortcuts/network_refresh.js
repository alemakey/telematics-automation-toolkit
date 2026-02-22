// ============================================================
//  network_refresh.js — Scriptable (iOS) Network Status Checker
//  Author  : alemakey
//  Version : 1.0.0
//  Requires: Scriptable app (https://scriptable.app/)
// ============================================================
//
//  DESCRIPTION:
//  Sends a lightweight HTTP GET request to a configurable
//  endpoint to verify internet/network reachability.
//  Displays the result as an iOS notification and, when run
//  as a widget, renders a status badge on the Home Screen.
//
//  USAGE:
//  1. Paste this script into a new Scriptable script.
//  2. Adjust CONFIG values below to match your environment.
//  3. Run manually, schedule via Shortcuts, or add as a widget.
// ============================================================

// ─── CONFIGURATION ─────────────────────────────────────────
const CONFIG = {
  // Target endpoint — change to your router admin page,
  // a local server, or a reliable public host.
  targetURL: "https://1.1.1.1",          // Cloudflare DNS (public fallback)
  // targetURL: "http://192.168.1.1",    // Example: local router

  timeoutSeconds: 10,                    // Max wait time before marking as unreachable
  scriptName:     "Network Refresh",     // Display name in notifications
};
// ───────────────────────────────────────────────────────────

/**
 * Performs the HTTP health check.
 * @returns {Promise<{reachable: boolean, statusCode: number|null, latencyMs: number}>}
 */
async function checkNetworkStatus() {
  const request = new Request(CONFIG.targetURL);
  request.timeoutInterval = CONFIG.timeoutSeconds;
  request.method          = "GET";

  const startTime = Date.now();

  try {
    const response = await request.loadString();
    const latencyMs = Date.now() - startTime;

    // HTTP status code is available via request.response.statusCode
    const statusCode = request.response?.statusCode ?? 200;

    return {
      reachable:  true,
      statusCode: statusCode,
      latencyMs:  latencyMs,
    };
  } catch (error) {
    return {
      reachable:  false,
      statusCode: null,
      latencyMs:  Date.now() - startTime,
      error:      error.message,
    };
  }
}

/**
 * Builds and presents a Scriptable notification with the result.
 * @param {{reachable: boolean, statusCode: number|null, latencyMs: number}} result
 */
async function showNotification(result) {
  const notification = new Notification();
  notification.scriptName = CONFIG.scriptName;

  if (result.reachable) {
    notification.title    = "✅ Network Reachable";
    notification.subtitle = `${CONFIG.targetURL}`;
    notification.body     = `Status: ${result.statusCode} | Latency: ${result.latencyMs} ms`;
  } else {
    notification.title    = "❌ Network Unreachable";
    notification.subtitle = `${CONFIG.targetURL}`;
    notification.body     = `Could not connect after ${CONFIG.timeoutSeconds}s.`;
  }

  await notification.schedule();
}

/**
 * Renders a simple Home Screen widget with network status.
 * @param {{reachable: boolean, latencyMs: number}} result
 */
function buildWidget(result) {
  const widget = new ListWidget();

  // Background gradient
  const gradient      = new LinearGradient();
  gradient.locations  = [0, 1];
  gradient.colors     = result.reachable
    ? [new Color("#1a1a2e"), new Color("#16213e")]   // dark-blue (online)
    : [new Color("#2e1a1a"), new Color("#3e1616")];  // dark-red (offline)
  widget.backgroundGradient = gradient;
  widget.setPadding(12, 14, 12, 14);

  // Status icon
  const iconText  = widget.addText(result.reachable ? "📡" : "🔴");
  iconText.font   = Font.systemFont(28);
  iconText.centerAlignText();
  widget.addSpacer(6);

  // Status label
  const statusLabel      = widget.addText(result.reachable ? "ONLINE" : "OFFLINE");
  statusLabel.font       = Font.boldSystemFont(16);
  statusLabel.textColor  = result.reachable ? Color.green() : Color.red();
  statusLabel.centerAlignText();
  widget.addSpacer(4);

  // Latency / detail
  const detail      = widget.addText(
    result.reachable ? `${result.latencyMs} ms` : "No connection"
  );
  detail.font       = Font.systemFont(11);
  detail.textColor  = Color.gray();
  detail.centerAlignText();
  widget.addSpacer(6);

  // Timestamp
  const timestamp      = widget.addDate(new Date());
  timestamp.applyTimeStyle();
  timestamp.font       = Font.systemFont(9);
  timestamp.textColor  = Color.gray();
  timestamp.centerAlignText();

  return widget;
}

// ─── MAIN ENTRY POINT ──────────────────────────────────────
async function main() {
  const result = await checkNetworkStatus();

  if (config.runsInWidget) {
    // Running as a Home Screen widget
    const widget = buildWidget(result);
    Script.setWidget(widget);
    widget.presentSmall();
  } else {
    // Running manually or via Shortcuts
    await showNotification(result);

    // Quick Alert summary
    const alert = new Alert();
    alert.title   = result.reachable ? "✅ Reachable" : "❌ Unreachable";
    alert.message = result.reachable
      ? `Connected to ${CONFIG.targetURL}\nLatency: ${result.latencyMs} ms`
      : `Failed to reach ${CONFIG.targetURL}\n(timeout: ${CONFIG.timeoutSeconds}s)`;
    alert.addAction("OK");
    await alert.present();
  }

  Script.complete();
}

await main();
