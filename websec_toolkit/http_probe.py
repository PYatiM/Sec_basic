from req_helper import safe_get

def probe(urls):
    for url in urls:
        r = safe_get(url)
        if r:
            print(f"{url} -> {r.status_code}")
        else:
            print(f"{url} -> DOWN")


def run():
    file = input("Targets file: ")
    with open(file) as f:
        probe([line.strip() for line in f])