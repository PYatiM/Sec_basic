from req_helper import safe_get

def test(url, attempts=20):
    success = 0

    for _ in range(attempts):
        r = safe_get(url)
        if r and r.status_code == 200:
            success += 1

    print(f"Successful: {success}/{attempts}")


def run():
    url = input("Target URL: ")
    attempts = int(input("Attempts (default 20): ") or 20)
    test(url, attempts)