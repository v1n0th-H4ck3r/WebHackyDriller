import requests
from colorama import Fore
def get_server_info(url):
    print(Fore.RED + "---------------------Server software information---------------------")
    try:
        response = requests.get(url)
        if 'Server' in response.headers:
            server_info = response.headers['Server']
            print(Fore.GREEN + f"[+] Server software and version: {server_info}")
        else:
            print("Server information not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing URL: {url} - {e}")
    print(Fore.RED + "---------------------------------------------------------------------")


