import requests

def probe(urls):
    for url in urls:
        try:
            r = requests.get(url, timeout=3)
            print(f"{url} -> {r.status_code}")
        except:
            print(f"{url} -> DOWN")

if __name__ == "__main__":
    with open("targets.txt") as f:
        probe([line.strip() for line in f])