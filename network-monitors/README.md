# 🌐 Network Monitors

Scripts in this folder continuously observe the health of your network interfaces (Wi-Fi, LAN, and WAN).

## Scripts

| Script | Language | Description |
|---|---|---|
| `ping_watchdog.py` | Python | Polls a host at a configurable interval; logs drops and latency |
| `bandwidth_logger.sh` | Bash | Samples `ifstat` / `vnstat` output and writes to a CSV log |

## Usage

```bash
# Ping watchdog — monitor your default gateway every 5 seconds
python3 ping_watchdog.py --host 192.168.1.1 --interval 5

# Bandwidth logger — log eth0 usage every 10 seconds
bash bandwidth_logger.sh --iface eth0 --interval 10 --output bw_log.csv
```
