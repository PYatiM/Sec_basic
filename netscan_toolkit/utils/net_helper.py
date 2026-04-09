import socket

def safe_connect(host, port, timeout=2):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((host, port))
        return sock
    except:
        return None