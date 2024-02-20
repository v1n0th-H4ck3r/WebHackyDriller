import re
import urllib.request
from urllib.parse import urljoin
from html.parser import HTMLParser
from colorama import Fore
class EmailParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.emails = []

    def handle_data(self, data):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, data)
        self.emails.extend(emails)

def extract_emails_from_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
            email_parser = EmailParser()
            email_parser.feed(html_content)
            return email_parser.emails
    except Exception as e:
        pass
        return []

def crawl_website(url):
    print(Fore.RED + "----------------------------Email crawler----------------------------")
    visited_urls = set()
    urls_to_visit = [url]

    while urls_to_visit:
        current_url = urls_to_visit.pop(0)
        if current_url in visited_urls:
            continue

        visited_urls.add(current_url)

        emails = extract_emails_from_url(current_url)
        if emails:
            for email in emails:
                print(Fore.GREEN + "[+] " + email + " - " + f"found at {current_url}")

        try:
            with urllib.request.urlopen(current_url) as response:
                html_content = response.read().decode('utf-8')
                links = re.findall(r'href=[\'"]?([^\'" >]+)', html_content)
                for link in links:
                    absolute_link = urljoin(current_url, link)
                    if absolute_link not in visited_urls:
                        urls_to_visit.append(absolute_link)
        except Exception as e:
            pass
        