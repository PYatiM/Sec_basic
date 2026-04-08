from http_probe import run as probe
from dir_fuzzer import run as fuzz
from header_analyzer import run as headers
from par_miner import run as params
from rate_test import run as rate


def menu():
    print("\n=== WEBSEC TOOLKIT ===")
    print("1. HTTP Probe")
    print("2. Directory Fuzzer")
    print("3. Header Analyzer")
    print("4. Parameter Miner")
    print("5. Rate Limit Tester")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = input("Select option: ")

        match choice:
            case "1":
                probe()
            case "2":
                fuzz()
            case "3":
                headers()
            case "4":
                params()
            case "5":
                rate()
            case "0":
                print("Exiting...")
                break
            case _:
                print("Invalid option")


if __name__ == "__main__":
    main()