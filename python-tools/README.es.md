# 🐍 Python Tools

🌍 [Read in English](README.md) | [Leer en Español](README.es.md)

Utilidades en Python para gestión avanzada de redes, cálculo de subredes y sondeo SNMP.

## Scripts

| Script | Descripción |
|---|---|
| `subnet_calculator.py` | Desglosa una notación CIDR en rango de hosts, broadcast y máscara |
| `snmp_poller.py` | Consulta OIDs SNMP en un dispositivo y muestra una tabla formateada |

## Uso

```bash
# Instalar dependencias primero
pip install -r ../requirements.txt

# Calcular información de subred
python3 subnet_calculator.py 192.168.10.0/24

# Consultar sysDescr SNMP de un dispositivo
python3 snmp_poller.py --host 192.168.1.1 --community public --oid 1.3.6.1.2.1.1.1.0
```
