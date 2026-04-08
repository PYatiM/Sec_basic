import requests

def test(url, attempts=20):
    success = 0
    for i in range(attempts):
        r = requests.get(url)
        if r.status_code == 200:
            success += 1

    print(f"Successful requests: {success}/{attempts}")

if __name__ == "__main__":
    test("http://example.com/login")