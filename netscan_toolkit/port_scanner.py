from utils.net_helper import safe_connect

def scan(host, ports):
    for port in ports:
        sock = safe_connect(host, port)
        if sock:
            print(f"[+] Open: {port}")
            sock.close()

def run():
    host = input("Host: ")
    ports = range(1, 1025)
    scan(host, ports)