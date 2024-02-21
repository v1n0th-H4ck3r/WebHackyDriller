import dns.resolver
from colorama import Fore
def dns_enum(domain):
    try:
        print(Fore.RED + "-----------------------------DNS records---------------------------")
        a_records = dns.resolver.query(domain, 'A')
        for record in a_records:
            print(Fore.GREEN + f"[+] A -> {str(record)}")

        # Perform DNS AAAA record lookup
        a_records = dns.resolver.query(domain, 'AAAA')
        for record in a_records:
            print(Fore.GREEN + f"[+] AAAA -> {str(record)}")

        # Perform DNS MX record lookup
        mx_records = dns.resolver.query(domain, 'MX')
        for record in mx_records:
            print(Fore.GREEN + f"[+] MX -> {str(record)}")

        # Perform DNS NS record lookup
        ns_records = dns.resolver.query(domain, 'NS')
        for record in ns_records:
            print(Fore.GREEN + f"[+] NS -> {str(record)}")

        # Perform DNS TXT record lookup
        txt_records = dns.resolver.query(domain, 'TXT')
        for record in txt_records:
            print(Fore.GREEN + f"[+] TXT -> {str(record)}")

        print(Fore.RED + "--------------------------------------------------------------------")
    except dns.resolver.NoAnswer:
        print(Fore.YELLOW + "[-] No DNS records found.")
        return True
    except dns.resolver.NXDOMAIN:
        print(Fore.YELLOW + "[-] No such domain exists.")
        return True
    except dns.resolver.Timeout:
        print(Fore.YELLOW + "[-] DNS query timed out.")
        return True
    except dns.resolver.NoNameservers:
        print(Fore.YELLOW + "[-] No nameservers found for the domain.")
        return True
    except Exception as e:
        print(Fore.MAGENTA + "[❌] An error occurred:", e)
        return True
