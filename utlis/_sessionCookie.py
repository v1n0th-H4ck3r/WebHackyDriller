import requests 
from colorama import Fore
def cookie(url):
    print(Fore.RED + "----------------------------Session Cookie----------------------------")
    # initialize a session 
    session = requests.Session() 
    
    # send a get request to the server 
    response = session.get(url) 
    
    # print the response dictionary 
    print(Fore.GREEN + f"{session.cookies.get_dict()}") 
    print(Fore.RED + "---------------------------------------------------------------------")
