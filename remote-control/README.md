# 🖥️ Remote Control

Utilities for remotely managing devices on your network — from Wake-on-LAN to VNC sessions.

## Scripts

| Script | Description |
|---|---|
| `wake_on_lan.py` | Sends a WoL magic packet to wake a device by MAC address |
| `vnc_launcher.sh` | Wrapper to start a VNC session with configurable options |

## Usage

```bash
# Wake a machine by its MAC address
python3 wake_on_lan.py --mac AA:BB:CC:DD:EE:FF --broadcast 192.168.1.255

# Launch a VNC session to a host
bash vnc_launcher.sh --host 192.168.1.50 --port 5900 --viewer tigervnc
```
