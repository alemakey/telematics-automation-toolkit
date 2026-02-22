# 🐚 Bash Utilities

🌍 [Read in English](README.md) | [Leer en Español](README.es.md)

Scripts de shell de propósito general para administración de redes y gestión de sistemas.

## Scripts

| Script | Descripción |
|---|---|
| `ssh_tunnel.sh` | Crea un túnel SSH local/remoto con un solo comando |
| `port_scanner.sh` | Escáner de puertos ligero para rangos CIDR usando `nc` / `nmap` |

## Uso

```bash
# Crear un túnel local: redirigir el puerto local 8080 → remoto 80
bash ssh_tunnel.sh --user admin --host 192.168.1.100 --local-port 8080 --remote-port 80

# Escanear puertos comunes en la red local
bash port_scanner.sh --range 192.168.1.0/24 --ports 22,80,443,8080
```

> **Consejo:** Haz los scripts ejecutables una sola vez con `chmod +x *.sh` para usarlos directamente.
