import socket

def enumerate(domain):
    subs = ["www", "mail", "ftp", "api"]

    for sub in subs:
        try:
            ip = socket.gethostbyname(f"{sub}.{domain}")
            print(f"[+] {sub}.{domain} -> {ip}")
        except:
            pass

def run():
    enumerate(input("Domain: "))