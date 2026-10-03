# Create a beginner-friendly Python port scanner of 15 lines.
# Ask the user for an IP address and a range of ports.
# Use sockets to check whether each port is open.
# Display the open and closed ports.
# Include error handling and comments.

import socket
def scan_ports(ip, start_port, end_port):
    open_ports = []
    closed_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((ip, port))  # Try to connect to the port
        if result == 0:
            open_ports.append(port)  # Port is open
        else:
            closed_ports.append(port)  # Port is closed
        sock.close()  # Close the socket
    return open_ports, closed_ports
if __name__ == "__main__":
    ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    try:
        open_ports, closed_ports = scan_ports(ip, start_port, end_port)
        print(f"Open ports: {open_ports}")
        print(f"Closed ports: {closed_ports}")
    except Exception as e:
        print(f"An error occurred: {e}")

