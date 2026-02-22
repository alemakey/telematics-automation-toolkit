# 📡 Telematics Automation Toolkit

[![GitHub License](https://img.shields.io/github/license/alemakey/telematics-automation-toolkit?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Bash](https://img.shields.io/badge/Bash-5.x-4EAA25?style=flat-square&logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![Scriptable](https://img.shields.io/badge/Scriptable-iOS-black?style=flat-square&logo=apple&logoColor=white)](https://scriptable.app/)

🌍 [Read in English](README.md) | [Leer en Español](README.es.md)

> Una colección curada de scripts de automatización, utilidades de gestión de redes y herramientas de control remoto — desarrollada por un **estudiante de Ingeniería en Telemática** para resolver desafíos reales de infraestructura.

---

## 🧭 Propósito

Este repositorio funciona como un kit de herramientas práctico para la **automatización de redes, gestión remota de sistemas y scripting multiplataforma**. Está diseñado para simplificar tareas telemáticas repetitivas, monitorear la salud de la red y ampliar el control de dispositivos mediante interfaces móviles y de línea de comandos.

Ya sea que estés diagnosticando una conexión Wi-Fi inestable, programando actualizaciones de red desde tu iPhone o automatizando sesiones SSH — este toolkit te tiene cubierto.

---

## 📁 Estructura del Repositorio

```
telematics-automation-toolkit/
│
├── network-monitors/          # Scripts para monitorear Wi-Fi, LAN y conectividad a internet
│   ├── ping_watchdog.py       # Monitor de ping continuo con soporte de alertas
│   ├── bandwidth_logger.sh    # Registra el uso de ancho de banda a lo largo del tiempo
│   └── README.md
│
├── ios-shortcuts/             # Automatizaciones e atajos para Scriptable (iOS)
│   ├── network_refresh.js     # Esqueleto de verificación HTTP y actualización de red
│   └── README.md
│
├── bash-utilities/            # Scripts Bash de propósito general para administración de sistemas
│   ├── ssh_tunnel.sh          # Asistente rápido para túneles SSH
│   ├── port_scanner.sh        # Escáner de puertos ligero para redes locales
│   └── README.md
│
├── python-tools/              # Scripts Python para gestión de redes y automatización
│   ├── subnet_calculator.py   # Herramienta de desglose de subredes CIDR
│   ├── snmp_poller.py         # Poller de dispositivos SNMP v2c
│   └── README.md
│
├── remote-control/            # Utilidades para gestión remota de dispositivos
│   ├── wake_on_lan.py         # Envío de paquetes mágicos Wake-on-LAN
│   ├── vnc_launcher.sh        # Wrapper para lanzar sesiones VNC
│   └── README.md
│
└── README.md                  ← Versión en inglés
```

---

## 🛠️ Tecnologías y Herramientas

| Categoría               | Tecnologías                                                                        |
|-------------------------|------------------------------------------------------------------------------------|
| **Lenguajes de Scripting** | Python 3, Bash / Shell, JavaScript (Scriptable)                                 |
| **Protocolos de Red**   | TCP/IP, ICMP (Ping), SNMP v2c/v3, SSH, Wake-on-LAN (WoL), DNS                    |
| **Automatización Móvil**| [Scriptable](https://scriptable.app/) (iOS), Apple Shortcuts                      |
| **Utilidades de Shell** | `shellmini`, `nmap`, `netcat`, `arp-scan`, `iproute2`                             |
| **Librerías Python**    | `scapy`, `paramiko`, `requests`, `pysnmp`, `netifaces`                            |
| **Plataformas**         | Linux (Debian/Ubuntu), macOS, iOS, Raspberry Pi (ARMv7/v8)                        |
| **Control de Versiones**| Git, GitHub Actions (CI para linting y pruebas)                                   |

---

## 🚀 Inicio Rápido

### Requisitos Previos

- **Python 3.10+** — [Descargar](https://python.org/downloads)
- **Bash 5.x** — Disponible nativamente en Linux/macOS; usar WSL2 en Windows
- **Scriptable** — [App Store](https://apps.apple.com/app/scriptable/id1405459188) (iOS/iPadOS)
- **Git** — `sudo apt install git` o [git-scm.com](https://git-scm.com)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/alemakey/telematics-automation-toolkit.git
cd telematics-automation-toolkit

# (Opcional) Crear un entorno virtual de Python
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias de Python
pip install -r requirements.txt
```

### Ejemplo de Ejecución

```bash
# Monitorear el gateway con el watchdog de ping
python3 network-monitors/ping_watchdog.py --host 192.168.1.1 --interval 5

# Ejecutar el escáner de puertos en la subred local
bash bash-utilities/port_scanner.sh 192.168.1.0/24
```

---

## 📱 Integración con iOS / Scriptable

Los scripts en `/ios-shortcuts` están diseñados para la aplicación **[Scriptable](https://scriptable.app/)** en iOS/iPadOS. Permiten:

- Ejecutar verificaciones de salud de red directamente desde tu iPhone/iPad
- Disparar automatizaciones a través de la app Atajos de Apple
- Mostrar widgets de estado de red en la pantalla de inicio

Para usarlos: copia el contenido del archivo `.js` en un nuevo script de Scriptable, o impórtalo a través de iCloud Drive.

---

## 🗺️ Hoja de Ruta

- [ ] Añadir listener de traps SNMP
- [ ] Crear un generador de mapas de calor de señal Wi-Fi (Python + matplotlib)
- [ ] Desarrollar un widget iOS para visualización de ancho de banda en tiempo real
- [ ] Agregar flujo de trabajo de GitHub Actions para linting (ShellCheck, pylint)
- [ ] Integrar GPIO de Raspberry Pi para indicadores físicos del estado de la red

---

## 👤 Autor

**Victor / alemakey**
> Estudiante de Ingeniería en Telemática | Entusiasta de la Automatización de Redes

[![GitHub](https://img.shields.io/badge/GitHub-alemakey-181717?style=flat-square&logo=github)](https://github.com/alemakey)

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** — consulta el archivo [LICENSE](LICENSE) para más detalles.

---

*Construido con ☕ y pasión por las redes.*
