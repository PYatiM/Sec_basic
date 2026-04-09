from utils.net_helper import safe_connect

def grab(host, port):
    sock = safe_connect(host, port)
    if sock:
        try:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024)
            print(f"[+] {host}:{port} -> {banner.decode(errors='ignore')}")
        except:
            pass
        finally:
            sock.close()

def run():
    grab(input("Host: "), int(input("Port: ")))