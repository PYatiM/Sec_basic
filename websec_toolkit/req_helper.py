import requests

def safe_get(url, timeout=3):
    try:
        return requests.get(url, timeout=timeout)
    except:
        return None