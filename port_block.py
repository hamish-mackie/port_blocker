#!/usr/bin/env python3
#coding=utf-8

import subprocess
import argparse

# File to store blocked ports
blocked_ports_file = 'blocked_ports.txt'

def block_ports(ports):
    with open(blocked_ports_file, 'a') as file:
        for port in ports:
            cmd = ["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"]
            subprocess.run(cmd)
            file.write(str(port) + '\n')
            print(f"Port {port} is now blocked.")

def unblock_all_ports():
    with open(blocked_ports_file, 'r+') as file:
        ports = file.readlines()
        for port in ports:
            port = port.strip()
            if port:
                cmd = ["sudo", "iptables", "-D", "INPUT", "-p", "tcp", "--dport", port, "-j", "DROP"]
                subprocess.run(cmd)
                print(f"Port {port} is now unblocked.")
        # Clear the file after unblocking all ports
        file.seek(0)
        file.truncate()

def main():
    parser = argparse.ArgumentParser(description="Block or unblock ports on your system.")
    parser.add_argument("action", choices=["block", "unblock"], help="Action to perform: block or unblock ports")
    parser.add_argument("ports", nargs='*', type=int, help="Port numbers to block (space-separated, required for blocking)")

    args = parser.parse_args()

    if args.action == "block":
        if args.ports:
            block_ports(args.ports)
        else:
            print("Port number(s) are required to block ports.")
    elif args.action == "unblock":
        unblock_all_ports()

if __name__ == "__main__":
    main()
