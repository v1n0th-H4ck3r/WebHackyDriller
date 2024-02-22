import requests
from bs4 import BeautifulSoup
from colorama import Fore
def get_javascript_libraries(url):
    print(Fore.RED + "-----------------------JavaScript libraries--------------------------")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        javascript_libraries = []

        # Find all script tags
        script_tags = soup.find_all('script')

        # Extract src attribute from script tags
        for script in script_tags:
            src = script.get('src')
            if src:
                # Extract filename from src URL
                filename = src.split('/')[-1]
                javascript_libraries.append(filename)

        return javascript_libraries
        
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None
