#!/usr/bin/env python3
from colorama import Fore, Back, Style, init
import os
import getpass


init()
user = getpass.getuser()
os.system("clear")
print(Fore.RED + f"ctf lab {user} | code by ovax  1.0")
print()
print()

x = str(input(Style.BRIGHT + "CTF | HTB or THM ?: "))
if x == "HTB":
    print('\033[3B'+"CTF HTB ")
    os.system("openvpn your path vpn here") # your vpn Hack the box

elif x == "THM":
    print('\033[3B'+"CTF THM ")
    os.system("openvpn your path vpn here") # your vpn Try hack me
