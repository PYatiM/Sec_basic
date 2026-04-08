from req_helper import safe_get

def mine(url, params_list):
    for param in params_list:
        test_url = f"{url}?{param}=test"
        r = safe_get(test_url)

        if r and (r.status_code == 200 or "error" in r.text.lower()):
            print(f"[+] Possible param: {param}")


def run():
    url = input("Target URL: ")
    file = input("Params wordlist: ")

    with open(file) as f:
        mine(url, [p.strip() for p in f])