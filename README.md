# Readme for Port Blocker Script

## Overview
This Python script provides a simple and efficient way to manage network port blocking on a system using `iptables`. It supports blocking specific ports as well as unblocking all previously blocked ports. This tool is particularly useful for network administrators or anyone needing to control access to their system's network services.

## Requirements
- Python 3
- `iptables` installed and configured on the system
- Root privileges for running the script (due to `sudo` usage in `iptables` commands)

## Installation
- Ensure Python 3 is installed on your system.
- Clone or download this script to your preferred directory.
- Ensure the script (`port_blocker.py`) is executable: `chmod +x port_blocker.py`

## Usage
The script can be used to block or unblock ports as follows:

### Blocking Ports
To block one or more ports, run the script with the `block` action followed by the port numbers:

```bash
./port_blocker.py block 80 443
```

This command will block ports 80 and 443.

### Unblocking All Ports
To unblock all previously blocked ports:

```bash
./port_blocker.py unblock
```

This command will unblock all ports that were blocked using this script.

## How it Works
- When blocking ports, the script appends rules to `iptables` to drop incoming TCP packets on the specified ports.
- The blocked ports are logged in a file (`blocked_ports.txt`) for reference.
- When unblocking, the script reads the `blocked_ports.txt` file, removes corresponding rules from `iptables`, and clears the file.

## Caution
- Blocking ports can affect network services and applications. Ensure you understand the implications of blocking a port before doing so.
- Running this script requires root privileges, which should be handled with care.

## License
This script is distributed under the MIT License. See `LICENSE` file for more details.

---

## Contributing
Contributions to improve the script or documentation are welcome. Please submit pull requests or open issues for any bugs or feature requests.

## Support
For any questions or support, raise an issue in the repository or contact the maintainer.

---