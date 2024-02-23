import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from colorama import Fore

async def is_login_form(form):
    # Check if form has username/email and password input fields
    has_username_field = form.find('input', {'type': 'text'}) or form.find('input', {'type': 'email'})
    has_password_field = form.find('input', {'type': 'password'})
    return has_username_field and has_password_field

async def get_forms(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

                forms = soup.find_all('form')
                form_count = len(forms)

                hidden_count = 0
                file_upload_count = 0
                button_count = 0
                login_form_count = 0
                for form in forms:
                    input_fields = form.find_all('input')
                    for input_field in input_fields:
                        # Check if input field is hidden or disabled
                        if input_field.get('type') == 'hidden' or input_field.get('disabled') is not None:
                            hidden_count += 1
                        # Check if input field is for file upload
                        elif input_field.get('type') == 'file':
                            file_upload_count += 1

                    # Count all button types
                    buttons = form.find_all('button')
                    for button in buttons:
                        button_count += 1

                    # Count button input fields with type="submit"
                    submit_buttons = form.find_all('input', {'type': 'submit'})
                    button_count += len(submit_buttons)

                    if await is_login_form(form):
                        login_form_count += 1

                return {
                    "form_count": form_count,
                    "hidden_count": hidden_count,
                    "file_upload_count": file_upload_count,
                    "button_count": button_count,
                    "login_form_count": login_form_count
                }
    except Exception as e:
        print("Error occurred..",end="\r")
        return None

def extract_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme + "://" + parsed_url.netloc

async def crawl(url, domain, visited=None):
    if visited is None:
        visited = set()

    if url in visited:
        return
    visited.add(url)

    if extract_domain(url) != domain:
        return

    forms_info = await get_forms(url)
    if forms_info is not None:
        print(Fore.GREEN + f"[+] {url}\n - Total Forms: {forms_info['form_count']} - Hidden Fields: {forms_info['hidden_count']} - File Upload Fields: {forms_info['file_upload_count']} - Button Count: {forms_info['button_count']} - Login Form Count: {forms_info['login_form_count']}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')
                links = soup.find_all('a', href=True)
                tasks = []
                for link in links:
                    next_url = urljoin(url, link['href'])
                    task = asyncio.ensure_future(crawl(next_url, domain, visited))
                    tasks.append(task)
                await asyncio.gather(*tasks)
    except Exception as e:
        pass

def subdirforms(url):
    domain = extract_domain(url)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(crawl(url, domain))
