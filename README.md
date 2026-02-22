# 📡 Telematics Automation Toolkit

[![GitHub License](https://img.shields.io/github/license/alemakey/telematics-automation-toolkit?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Bash](https://img.shields.io/badge/Bash-5.x-4EAA25?style=flat-square&logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![Scriptable](https://img.shields.io/badge/Scriptable-iOS-black?style=flat-square&logo=apple&logoColor=white)](https://scriptable.app/)

🌍 [Read in English](README.md) | [Leer en Español](README.es.md)

> A curated collection of automation scripts, network management utilities, and remote control tools — built by a **Telecommunications Engineering student** to tackle real-world infrastructure challenges.

---

## 🧭 Purpose

This repository serves as a practical toolkit for **network automation, remote system management, and cross-platform scripting**. It is designed to simplify repetitive telematic tasks, monitor network health, and extend device control through mobile and shell-based interfaces.

Whether you're diagnosing a flaky Wi-Fi connection, scheduling network refreshes from your iPhone, or automating SSH sessions — this toolkit has you covered.

---

## 📁 Repository Structure

```
telematics-automation-toolkit/
│
├── network-monitors/          # Scripts to monitor Wi-Fi, LAN, and internet health
│   ├── ping_watchdog.py       # Continuous ping monitor with alert support
│   ├── bandwidth_logger.sh    # Logs bandwidth usage over time
│   └── README.md
│
├── ios-shortcuts/             # Scriptable (iOS) automations and shortcuts
│   ├── network_refresh.js     # HTTP check & network refresh skeleton
│   └── README.md
│
├── bash-utilities/            # General-purpose Bash scripts for sysadmin tasks
│   ├── ssh_tunnel.sh          # Quick SSH tunnel helper
│   ├── port_scanner.sh        # Lightweight local network port scanner
│   └── README.md
│
├── python-tools/              # Python scripts for network management & automation
│   ├── subnet_calculator.py   # CIDR subnet breakdown tool
│   ├── snmp_poller.py         # SNMP v2c device poller
│   └── README.md
│
├── remote-control/            # Remote device management utilities
│   ├── wake_on_lan.py         # Wake-on-LAN magic packet sender
│   ├── vnc_launcher.sh        # VNC session launcher wrapper
│   └── README.md
│
└── README.md                  ← You are here
```

---

## 🛠️ Technologies & Tools

| Category              | Technologies                                                                 |
|-----------------------|------------------------------------------------------------------------------|
| **Scripting Languages** | Python 3, Bash / Shell, JavaScript (Scriptable)                            |
| **Network Protocols** | TCP/IP, ICMP (Ping), SNMP v2c/v3, SSH, Wake-on-LAN (WoL), DNS               |
| **Mobile Automation** | [Scriptable](https://scriptable.app/) (iOS), Apple Shortcuts                |
| **Shell Utilities**   | `shellmini`, `nmap`, `netcat`, `arp-scan`, `iproute2`                        |
| **Python Libraries**  | `scapy`, `paramiko`, `requests`, `pysnmp`, `netifaces`                      |
| **Platforms**         | Linux (Debian/Ubuntu), macOS, iOS, Raspberry Pi (ARMv7/v8)                  |
| **Version Control**   | Git, GitHub Actions (CI for linting and testing)                             |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** — [Download](https://python.org/downloads)
- **Bash 5.x** — Available natively on Linux/macOS; use WSL2 on Windows
- **Scriptable** — [App Store](https://apps.apple.com/app/scriptable/id1405459188) (iOS/iPadOS)
- **Git** — `sudo apt install git` or [git-scm.com](https://git-scm.com)

### Installation

```bash
# Clone the repository
git clone https://github.com/alemakey/telematics-automation-toolkit.git
cd telematics-automation-toolkit

# (Optional) Create a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### Running a script example

```bash
# Monitor your gateway with the ping watchdog
python3 network-monitors/ping_watchdog.py --host 192.168.1.1 --interval 5

# Run the port scanner on your local subnet
bash bash-utilities/port_scanner.sh 192.168.1.0/24
```

---

## 📱 iOS / Scriptable Integration

Scripts in `/ios-shortcuts` are designed for the **[Scriptable](https://scriptable.app/)** app on iOS/iPadOS. They allow you to:

- Run network health checks directly from your iPhone/iPad
- Trigger automations via the Apple Shortcuts app
- Display network status widgets on your Home Screen

To use them: copy the `.js` file content into a new Scriptable script, or import via iCloud Drive.

---

## 🗺️ Roadmap

- [ ] Add SNMP trap listener
- [ ] Build a Wi-Fi signal strength heatmap generator (Python + matplotlib)
- [ ] Create an iOS widget for real-time bandwidth display
- [ ] Add GitHub Actions workflow for script linting (ShellCheck, pylint)
- [ ] Integrate Raspberry Pi GPIO for physical network status indicators

---

## 👤 Author

**Victor / alemakey**
> Telecommunications Engineering Student | Network Automation Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-alemakey-181717?style=flat-square&logo=github)](https://github.com/alemakey)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

*Built with ☕ and a passion for networks.*
