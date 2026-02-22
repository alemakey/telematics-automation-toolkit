# 🌐 Network Monitors

🌍 [Read in English](README.md) | [Leer en Español](README.es.md)

Los scripts de esta carpeta monitorean de forma continua la salud de las interfaces de red (Wi-Fi, LAN y WAN).

## Scripts

| Script | Lenguaje | Descripción |
|---|---|---|
| `ping_watchdog.py` | Python | Hace ping a un host en intervalos configurables; registra pérdidas y latencia |
| `bandwidth_logger.sh` | Bash | Muestrea la salida de `ifstat` / `vnstat` y escribe los datos en un log CSV |
| `wifi_monitor.py` | Python | Escáner de red local basado en ARP; alerta sobre MACs desconocidas (detección de intrusos) |

## Uso

```bash
# Ping watchdog — monitorear el gateway cada 5 segundos
python3 ping_watchdog.py --host 192.168.1.1 --interval 5

# Registrador de ancho de banda — loguear eth0 cada 10 segundos
bash bandwidth_logger.sh --iface eth0 --interval 10 --output bw_log.csv

# Monitor de intrusos Wi-Fi — escaneo único
python3 wifi_monitor.py

# Monitor de intrusos Wi-Fi — bucle continuo cada 30 s
python3 wifi_monitor.py --loop --interval 30
```
