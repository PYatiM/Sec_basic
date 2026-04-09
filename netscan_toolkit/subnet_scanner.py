from utils.net_helper import safe_connect

def scan_subnet(base_ip):
    for i in range(1, 255):
        host = f"{base_ip}.{i}"
        sock = safe_connect(host, 80, timeout=0.5)
        if sock:
            print(f"[+] Alive: {host}")
            sock.close()

def run():
    scan_subnet(input("Base IP (e.g., 192.168.1): "))