"""
WARNING:
This tool is for educational purposes only.
Do not use it on networks or systems without permission.
By : AbdulelahAlotibe
GitHub url https://github.com/WhiteeHawk
"""

from utility import get_service, try_banner
from colorama import Fore, Style, init
import json
import socket
import threading
import ipaddress
import argparse

init()

# ---------------- CLI ----------------
parser = argparse.ArgumentParser(description="Advanced Port Scanner")

parser.add_argument("-t", "--target", help="Target IP or domain")
parser.add_argument("-p", "--ports", default="1-1024", help="Port range")

args = parser.parse_args()

# ---------------- INPUT OR CLI ----------------
if not args.target:
    print("""
    🔐 Advanced Port Scanner
    ------------------------
    Author: Abdulelah Alotibe
    Usage: Authorized testing only
    """)

    target = input(" Enter target IP or domain: ")
    port_range = input(" Enter port range (default 1-1024): ") or "1-1024"

else:
    target = args.target
    port_range = args.ports

# ---------------- VALIDATION ----------------
try:
    ipaddress.ip_address(target)
except ValueError:
    try:
        target = socket.gethostbyname(target)
    except Exception:
        print("❌ Invalid target")
        exit()

print(f"\n Target: {target}")
print(" Scanning started...\n")
print("-" * 40)

# ---------------- HELPERS ----------------
def parse_ports(port_range):
    start, end = port_range.split("-")
    return range(int(start), int(end) + 1)

open_ports = []
lock = threading.Lock()

# ---------------- SCAN ----------------
open_ports = []
lock = threading.Lock()

total_ports = len(list(parse_ports(port_range)))
scanned = 0

def scan_port(port):
    try:
        s = socket.socket()
        s.settimeout(1)

        if s.connect_ex((target, port)) == 0:
            service = get_service(port)
            banner = try_banner(s)

            result = {
                "port": port,
                "service": service,
                "banner": banner
            }

            with lock:
                print(Fore.GREEN + f"🔓 OPEN | {port} | {service} | {banner}" + Style.RESET_ALL)
                open_ports.append(result)

        s.close()

    except Exception:
        pass

# ---------------- THREADING ----------------
threads = []

for port in parse_ports(port_range):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


# ---------------- SAVE ----------------
with open("results.txt", "w") as f:
    for item in open_ports:
        f.write(f"{item['port']} | {item['service']} | {item['banner']}\n")

print("\n[+] Results saved to results.txt")
print(f"[+] Total open ports: {len(open_ports)}")