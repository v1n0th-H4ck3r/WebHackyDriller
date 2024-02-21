import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from colorama import Fore

def get_subdirectories(url):
    print(Fore.RED + "------------------------Subdirectories Findings----------------------")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            subdirectories = set()
            parsed_url = urlparse(url)
            base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('/') or href.startswith('./'):
                    subdirectories.add(urljoin(base_url, href))
                elif parsed_url.netloc in href:
                    subdirectories.add(href)
            return subdirectories
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
            return set()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return set()

