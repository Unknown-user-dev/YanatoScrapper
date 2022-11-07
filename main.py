import colorama
import os
import requests
from bs4 import BeautifulSoup 
from colorama import Fore, Back, Style
from colorama import init
os.system("cls || clear") 
init()
banner = Fore.RED + f"""
 __     __               _        _____                                      
 \ \   / /              | |      / ____|                                     
  \ \_/ /_ _ _ __   __ _| |_ ___| (___   ___ _ __ __ _ _ __  _ __   ___ _ __ 
   \   / _` | '_ \ / _` | __/ _ \\___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|
    | | (_| | | | | (_| | || (_) |___) | (__| | | (_| | |_) | |_) |  __/ |   
    |_|\__,_|_| |_|\__,_|\__\___/_____/ \___|_|  \__,_| .__/| .__/ \___|_|   
                                                      | |   | |              
                                                      |_|   |_|                                                       
                                                                 
            By : @Unknown-user-dev 
        https://github.com/Unknown-user-dev
"""

print(banner)
def menu():
    print(Fore.GREEN + """
    [1] Avoir la liste de tout les Proxy
    [2] Credits
    [3] Quitter
    """)
    choice = input(Fore.BLUE + "Choisissez une option : ")
    if choice == "1":
        os.system("cls || clear")
        print(banner)
        print(Fore.GREEN + "Récupération des Proxy...")
        url = "https://sslproxies.org/" 
        response = requests.get(url)
        tbody = BeautifulSoup(response.text, "html.parser").find("tbody")
        trs = tbody.find_all("tr")
        for tr in trs:
            tds = tr.find_all("td")
            ip = tds[0].text
            port = tds[1].text
            proxy = ip + ":" + port
            print(Fore.BLUE + proxy)
        print(Fore.GREEN + "Fin de la récupération des Proxy")
        input(Fore.BLUE + "Appuyez sur Entrée pour revenir au menu...")
        os.system("cls || clear")
        print(banner)
        menu()
    elif choice == "2":
        print(Fore.GREEN + "By : @Unknown-user-dev | github.com/Unknown-user-dev | >_Unknown User#8624 ")
        print(banner)
        menu()
    elif choice == "3":
        print(Fore.RED + "Bye !")
        exit()
    else:
        print(Fore.RED + "Erreur : Veuillez saisir une option valide !")
        menu()
if __name__ == "__main__":
    menu()