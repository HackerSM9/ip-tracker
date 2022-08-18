import os,sys
import requests
import json

url = "http://ip-api.com/json/"
r = '\033[1;31m'
e = '\033[0m'
os.system('clear')
print ('''
\033[1;33m
  _____ _____           _______ _____            _____ _  ________ _____   
 |_   _|  __ \         |__   __|  __ \     /\   / ____| |/ /  ____|  __ \  
   | | | |__) | \-----\   | |  | |__) |   /  \ | |    | ' /| |__  | |__) | 
   | | |  ___/   \-----\  | |  |  _  /   / /\ \| |    |  < |  __| |  _  /  
  _| |_| |                | |  | | \ \  / ____ \ |____| . \| |____| | \ \  
 |_____|_|                |_|  |_|  \_\/_/    \_\_____|_|\_\______|_|  \_\ 
 
           <---[ \033[35mby HackerSM9 | Made In India | v.98.7\033[0m \033[1;33m]--->

1) Your IP\n2) Track IP\n3) More Tools\n4) About\n5) Upgrade\n\033[0m''')
print(r+">>> Exit tool [ CTRL + Z ] <<< \n"+e)

ip = int(input("\033[1;36mEnter Your Choice $ \033[1;36m"))
if ip == 1:
    	os.system('cd .src && php .ip-tracer.php')
if ip == 2:
    	print("")
    	os.system('cd .src && python3 track-ip.py')	
if ip == 3:
    	os.system('xdg-open https://github.com/HackerSM9')
if ip == 4:
        os.system('cd .src && python3 .a.py')
if ip == 5:
    	os.system('bash update')	
elif (ip >= 6):
    print(r+"Invalid Option Ó╭╮Ò"+e)
else:
    print("\033[1;46m\nDone !\033[0m")
    print("\n")
