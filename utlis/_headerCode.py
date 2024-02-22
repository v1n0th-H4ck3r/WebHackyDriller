import requests
from colorama import Fore
def get_headers(url):
    print(Fore.RED + "-------------------------------Header--------------------------------")
    try:
        response = requests.get(url)
        headers = response.headers
        return headers
    except requests.exceptions.RequestException as e:
        print(Fore.MAGENTA + "[❌]Error occurred:", e)
        return None

def print_headers(headers):
    if headers:
        for header, value in headers.items():
            print(Fore.GREEN + f"{header}: {value}")
    else:
        print(Fore.YELLOW + "[-] No headers retrieved.")

