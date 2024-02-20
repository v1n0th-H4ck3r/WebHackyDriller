import socket
from colorama import Fore
def check_dns_load_balancing(domain):
    print(Fore.RED + "-----------------------Load Balance Detector-------------------------")
    print(Fore.GREEN + "Checking for DNS load balancing...")
    try:
        ip_addresses = socket.gethostbyname_ex(domain)[-1]
        if len(ip_addresses) > 1:
            print(Fore.GREEN + "[+] DNS Load balancing detected.")
            print(Fore.GREEN + "[+] IP addresses associated with the domain:", ip_addresses)
        else:
            print(Fore.YELLOW + "[-] No DNS load balancing detected.")
    except socket.gaierror as e:
        return False, f"Error occurred: {str(e)}"
    print(Fore.RED + "---------------------------------------------------------------------")
