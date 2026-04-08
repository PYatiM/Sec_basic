import requests

def mine(url, params_list):
    for param in params_list:
        test_url = f"{url}?{param}=test"
        r = requests.get(test_url)

        if "error" in r.text.lower() or r.status_code == 200:
            print(f"[+] Possible param: {param}")

if __name__ == "__main__":
    with open("params.txt") as f:
        mine("http://example.com/page", [p.strip() for p in f])