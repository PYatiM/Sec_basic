from req_helper import safe_get

SEC_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]

def analyze(url):
    r = safe_get(url)
    if not r:
        print("Request failed")
        return

    for h in SEC_HEADERS:
        if h not in r.headers:
            print(f"[-] Missing: {h}")
        else:
            print(f"[+] Present: {h}")


def run():
    analyze(input("URL: "))