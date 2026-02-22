# 🐚 Bash Utilities

General-purpose shell scripts for network administration and system management.

## Scripts

| Script | Description |
|---|---|
| `ssh_tunnel.sh` | Creates a local/remote SSH tunnel with a single command |
| `port_scanner.sh` | Lightweight CIDR range port scanner using `nc` / `nmap` |

## Usage

```bash
# Create a local tunnel: forward local port 8080 → remote 80
bash ssh_tunnel.sh --user admin --host 192.168.1.100 --local-port 8080 --remote-port 80

# Scan common ports on your LAN
bash port_scanner.sh --range 192.168.1.0/24 --ports 22,80,443,8080
```

> **Tip:** Make scripts executable once with `chmod +x *.sh` to run them directly.
