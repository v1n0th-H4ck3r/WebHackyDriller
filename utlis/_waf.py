import requests
from colorama import Fore

class WAFingerprintingToolkit:
    def __init__(self):
        self.target_url = ""
    
    def set_target_url(self, url):
        self.target_url = url
    
    def check_waf(self):
        print(Fore.RED + "--------------------------WAF Footprints----------------------------")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response_normal = requests.get(self.target_url, headers=headers)
        response_attack = requests.get(self.target_url + "/<script>alert('XSS')</script>", headers=headers)
        print(Fore.GREEN + "Checking for WAF...")
        print(Fore.GREEN + "Normal response code:", response_normal.status_code)
        print(Fore.GREEN + "Attack response code:", response_attack.status_code)
        print(Fore.GREEN + "Normal response headers:", response_normal.headers)
        print(Fore.GREEN + "Attack response headers:", response_attack.headers)
        
        waf_detected = False
        waf_type = ""
        
        # Check for WAF based on response headers
        if "WAF" in response_normal.headers:
            waf_detected = True
            waf_type = response_normal.headers['WAF']
        elif "Server" in response_normal.headers and "WAF" in response_normal.headers['Server']:
            waf_detected = True
            waf_type = response_normal.headers['Server']
        
        # Check for WAF based on response code difference during attack
        if response_normal.status_code != response_attack.status_code:
            waf_detected = True
            waf_type += " (Possibly due to response code difference)"
        
        # Generate detection summary
        summary = f"[*] The site {self.target_url} seems to be "
        if waf_detected:
            summary += f"behind {waf_type}."
        else:
            summary += "not behind a WAF or some sort of security solution."
        return summary
    
