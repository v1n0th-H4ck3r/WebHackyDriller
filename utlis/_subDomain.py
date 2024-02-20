import requests
import socket
from colorama import Fore
def get_ip_address(subdomain):
    try:
        ip_address = socket.gethostbyname(subdomain)
        return ip_address
    except Exception as e:
        return None

def enumerate_subdomains(domain):
    print(Fore.RED + "------------------------Sub-domain Findings--------------------------")
    try:
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        response = requests.get(url)
        data = response.json()

        subdomains = set()
        for entry in data:
            name_value = entry.get('name_value', '')
            if name_value:
                ip_address = get_ip_address(name_value)
                if ip_address:
                    subdomains.add((name_value, ip_address))
        return list(subdomains)
    
    except Exception as e:
        print(f"Error: {e}")
        return []

