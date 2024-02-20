import dns.resolver
import socket
from colorama import Fore
from utlis import _dnsenum, _waf
def internet_check():
    try:
        socket.create_connection(("www.google.com", 80))
        print(Fore.GREEN + "\n[!] Internet Connection is Available!")
        return None
    except OSError:
        print(Fore.RED + "\n[=!] Warning! Internet Connection is Unavailable!")
        return None

def InfoGather():
    domainName = input("[+] Enter a specific URL to find pages linking to it (e.g., example.com): ")
    fullUrl = "https://" + domainName
    dnsQuery = _dnsenum.dns_enum(domainName)
    print(dnsQuery)
    waf_toolkit = _waf.WAFingerprintingToolkit()
    waf_toolkit.set_target_url(fullUrl)
    result = waf_toolkit.check_waf()
    print("[+] Generic Detection results:")
    print(result)
    print(Fore.RED + "----------------------------------------------------------------------")



def Scanner():
    print("Writing the scanner script...")


def vulnAss():
    print("Writing the vulnass script...")


def Exploit():
    print("Writing the exploit script...")


def main():
    print(Fore.CYAN + """
[+]    
|
|    ___ ___       __    ___ ___            __          ______        __ __ __            
|   |   Y   .-----|  |--|   Y   .---.-.----|  |--.--.--|   _  \ .----|__|  |  .-----.----.
|   |.  |   |  -__|  _  |.  1   |  _  |  __|    <|  |  |.  |   \|   _|  |  |  |  -__|   _|
|   |. / \  |_____|_____|.  _   |___._|____|__|__|___  |.  |    |__| |__|__|__|_____|__|  
|   |:      |           |:  |   |                |_____|:  1    /                         
|   |::.|:. |           |::.|:. |                      |::.. . /                          
|   `--- ---'           `--- ---'                      `------'                           
|   - By Vinoth (https://github.com/v1n0th-H4ck3r/WebHackyDriller.git)                                                                                    
|  
|
[+]
    """)
    internet_check()
    searchquery=""
    while 1:
        print(Fore.CYAN)
        print("[1] Information Gathering")
        print("[2] Scanning")
        print("[3] Vulnerability Assessment")
        print("[4] Exploitation")
        print("\n")
        query_type = input("[+] Select your option:\t")
        if query_type=="1":
            InfoGather()
        elif query_type == "2":
            Scanner()
        elif query_type == "3":
            vulnAss()
        elif query_type == "4":
            Exploit()
        else:
            print("\n")
            print(Fore.MAGENTA + "[❌] Warning - You have entered a unknown number to hack!")
if __name__ == '__main__':
    main() 