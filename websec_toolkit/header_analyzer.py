import requests

SEC_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]

def analyze(url):
    r = requests.get(url)
    headers = r.headers

    for h in SEC_HEADERS:
        if h not in headers:
            print(f"[-] Missing: {h}")
        else:
            print(f"[+] Present: {h}")

if __name__ == "__main__":
    analyze("http://example.com")