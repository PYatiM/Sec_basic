import socket

def sniff():
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sock.bind(("0.0.0.0", 0))
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print("[*] Sniffing...")
    while True:
        data, _ = sock.recvfrom(65535)
        print(data[:50])

def run():
    sniff()