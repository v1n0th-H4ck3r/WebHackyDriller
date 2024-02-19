import dns.resolver

def dns_enum(domain):
    try:
        # Perform DNS A record lookup
        a_records = dns.resolver.query(domain, 'A')
        print("A Records:")
        for record in a_records:
            print(record)

        # Perform DNS AAAA record lookup
        a_records = dns.resolver.query(domain, 'AAAA')
        print("AAAA Records:")
        for record in a_records:
            print(record)

        # Perform DNS MX record lookup
        mx_records = dns.resolver.query(domain, 'MX')
        print("\nMX Records:")
        for record in mx_records:
            print(record)

        # Perform DNS NS record lookup
        ns_records = dns.resolver.query(domain, 'NS')
        print("\nNS Records:")
        for record in ns_records:
            print(record)

        # Perform DNS TXT record lookup
        txt_records = dns.resolver.query(domain, 'TXT')
        print("\nTXT Records:")
        for record in txt_records:
            print(record)

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

if __name__ == "__main__":
    domain = input("Enter the domain to perform DNS enumeration: ")
    dns_enum(domain)
