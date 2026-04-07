import requests

def fuzz(base_url, wordlist):
    with open(wordlist) as f:
        for word in f:
            path = word.strip()
            url = f"{base_url}/{path}"
            try:
                r = requests.get(url)
                if r.status_code in [200, 301, 403]:
                    print(f"[+] Found: {url} ({r.status_code})")
            except:
                pass

if __name__ == "__main__":
    fuzz("http://example.com", "words.txt")