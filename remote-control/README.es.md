# 🖥️ Remote Control

🌍 [Read in English](README.md) | [Leer en Español](README.es.md)

Utilidades para gestionar dispositivos de forma remota en tu red — desde Wake-on-LAN hasta sesiones VNC.

## Scripts

| Script | Descripción |
|---|---|
| `wake_on_lan.py` | Envía un paquete mágico WoL para encender un dispositivo por dirección MAC |
| `vnc_launcher.sh` | Wrapper para iniciar sesiones VNC con opciones configurables |

## Uso

```bash
# Encender un dispositivo por su dirección MAC
python3 wake_on_lan.py --mac AA:BB:CC:DD:EE:FF --broadcast 192.168.1.255

# Iniciar una sesión VNC hacia un host
bash vnc_launcher.sh --host 192.168.1.50 --port 5900 --viewer tigervnc
```
