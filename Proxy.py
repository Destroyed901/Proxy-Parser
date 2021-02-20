import requests as r, os, threading
from threading import Thread
from colorama import Fore,Style
from termcolor import colored
import time

gey = colored("""
  _____                       _____                         
 |  __ \                     |  __ \                        
 | |__) | __ _____  ___   _  | |__) |_ _ _ __ ___  ___ _ __ 
 |  ___/ '__/ _ \ \/ / | | | |  ___/ _` | '__/ __|/ _ \ '__|
 | |   | | | (_) >  <| |_| | | |  | (_| | |  \__ \  __/ |   
 |_|   |_|  \___/_/\_\\__, | |_|   \__,_|_|  |___/\___|_|   
                       __/ |                                
                      |___/                                 
                                 Creators: https://t.me/termux999 
""", "blue")

print(gey)


time.sleep(5)

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def check(ip, prox):
	try:
		ipx = r.get("http://fsystem88.ru/ip", proxies={'http':'http://{}'.format(prox), 'https':'http://{}'.format(prox)}, verify=False, timeout=10).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.BLUE+"{} good!".format(prox))
		f = open("proxies.txt", "a+")
		f.write("{}\n".format(prox))
		f.close()
	else:
		#print(Fore.RED+"{} bad".format(prox))
		pass

url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http"
req = r.get(url)
ip = r.post("http://fsystem88.ru/ip").text
array = req.text.split()
clear()
print(Fore.LIGHTYELLOW_EX+"Your ip: {}".format(ip)+Style.RESET_ALL)
open("proxies.txt", "w+").close()
for prox in array:
	thread_list = []
	t = threading.Thread (target=check, args=(ip, prox))
	thread_list.append(t)
	t.start()

