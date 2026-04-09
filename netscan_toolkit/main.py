from port_scanner import run as portscan
from banner_grabber import run as banner
from packet_sniffer import run as sniff
from dns_enum import run as dns
from subnet_scanner import run as subnet


def menu():
    print("\n=== NETSCAN TOOLKIT ===")
    print("1. Port Scanner")
    print("2. Banner Grabber")
    print("3. Packet Sniffer")
    print("4. DNS Enumerator")
    print("5. Subnet Scanner")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = input("Select: ")

        match choice:
            case "1":
                portscan()
            case "2":
                banner()
            case "3":
                sniff()
            case "4":
                dns()
            case "5":
                subnet()
            case "0":
                break
            case _:
                print("Invalid")


if __name__ == "__main__":
    main()