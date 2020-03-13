#!/usr/bin/python

import time
import os
import sys
import getpass
import colorama
import requests
from colorama import Back, Fore, Style, deinit, init
init()

print(Fore.RED)


print(" ██████╗███████╗    ██████╗ ███████╗███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ ")
print("██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗")
print("██║     █████╗      ██████╔╝█████╗  ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝")
print("██║     ██╔══╝      ██╔══██╗██╔══╝  ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗")
print("╚██████╗██║         ██║  ██║███████╗███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║")
print(" ╚═════╝╚═╝         ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝")                                                                                 
print(Fore.GREEN)
print("                    --Cloudfare resolver-- [BY LAWLI3T]    ")
print(Fore.MAGENTA)
     
website=input('\bEnter website : ')
r = requests.get('https://webresolver.nl/api.php?key=5HUPH-I6VEP-TXBGM-3HL8L&action=cloudflare&string=' + website)
print(Fore.CYAN + "\nResult : ")
print(Fore.YELLOW)
print(r.text)      
