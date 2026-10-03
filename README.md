# Python Port Scanner

## Description

This project is a simple Python-based TCP port scanner. It checks a specified range of ports on an IP address and identifies which ports are open and which ports are closed.

## Features

* Takes an IP address from the user
* Takes a starting and ending port
* Scans each port in the given range
* Uses TCP connections to check the ports
* Displays open and closed ports
* Includes basic error handling

## Requirements

* Python 3
* Python's built-in `socket` library

No additional Python packages are required.

## How to Run

Open a terminal in the project folder and run:

```bash
python port_scanner.py
```

The program will ask for:

1. The IP address to scan
2. The starting port number
3. The ending port number

## How It Works

The program creates a TCP socket for each port and attempts to connect to it. If the connection is successful, the port is added to the open ports list. Otherwise, it is added to the closed ports list.

## Authorized Use

This tool should only be used on systems that you own or have explicit permission to test. For safe testing, `127.0.0.1` can be used to scan the local computer.
