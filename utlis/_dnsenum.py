import dns.resolver
from colorama import Fore
def dns_enum(domain):
    try:
        print(Fore.RED + "-----------------------------DNS records---------------------------")
        a_records = dns.resolver.query(domain, 'A')
        for record in a_records:
            print(Fore.GREEN + f"[A] -> {str(record)}")

        # Perform DNS AAAA record lookup
        a_records = dns.resolver.query(domain, 'AAAA')
        for record in a_records:
            print(Fore.GREEN + f"[AAAA] -> {str(record)}")

        # Perform DNS MX record lookup
        mx_records = dns.resolver.query(domain, 'MX')
        for record in mx_records:
            print(Fore.GREEN + f"[MX] -> {str(record)}")

        # Perform DNS NS record lookup
        ns_records = dns.resolver.query(domain, 'NS')
        for record in ns_records:
            print(Fore.GREEN + f"[NS] -> {str(record)}")

        # Perform DNS TXT record lookup
        txt_records = dns.resolver.query(domain, 'TXT')
        for record in txt_records:
            print(Fore.GREEN + f"[TXT] -> {str(record)}")

        print(Fore.RED + "--------------------------------------------------------------------")
    except dns.resolver.NoAnswer:
        print("No DNS records found.")
    except dns.resolver.NXDOMAIN:
        print("No such domain exists.")
    except dns.resolver.Timeout:
        print("DNS query timed out.")
    except dns.resolver.NoNameservers:
        print("No nameservers found for the domain.")
    except Exception as e:
        print("An error occurred:", e)
