from req_helper import safe_get

def fuzz(base_url, wordlist):
    with open(wordlist) as f:
        for word in f:
            path = word.strip()
            url = f"{base_url}/{path}"
            r = safe_get(url)

            if r and r.status_code in [200, 301, 403]:
                print(f"[+] Found: {url} ({r.status_code})")


def run():
    base = input("Base URL: ")
    wordlist = input("Wordlist file: ")
    fuzz(base, wordlist)