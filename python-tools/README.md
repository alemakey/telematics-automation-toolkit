# 🐍 Python Tools

Python utilities for advanced network management, subnet calculation, and SNMP polling.

## Scripts

| Script | Description |
|---|---|
| `subnet_calculator.py` | Breaks down a CIDR notation into host range, broadcast, mask |
| `snmp_poller.py` | Polls SNMP OIDs on a device and displays a formatted table |

## Usage

```bash
# Install dependencies first
pip install -r ../requirements.txt

# Calculate subnet info
python3 subnet_calculator.py 192.168.10.0/24

# Poll SNMP sysDescr from a device
python3 snmp_poller.py --host 192.168.1.1 --community public --oid 1.3.6.1.2.1.1.1.0
```
