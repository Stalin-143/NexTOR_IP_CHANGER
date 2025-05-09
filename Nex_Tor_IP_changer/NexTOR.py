# -*- coding: utf-8 -*-

import time
import os
import subprocess

try:
    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests requests[socks]')
    print('[!] python3 requests is installed ')

try:
    from stem import Signal
    from stem.control import Controller
except ImportError:
    print('[+] python3 stem is not installed')
    os.system('pip3 install stem')
    from stem import Signal
    from stem.control import Controller

try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install tor -y', shell=True)
    print('[!] Tor installed successfully')

os.system("clear")

def new_tor_identity():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  # Uses default cookie auth
            controller.signal(Signal.NEWNYM)
            print('[*] Requested new identity from Tor')
    except Exception as e:
        print(f"[!] Failed to request new identity: {e}")

def ma_ip():
    url = 'http://checkip.amazonaws.com'
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    get_ip = requests.get(url, proxies=proxies, timeout=10)
    return get_ip.text.strip()

def change():
    new_tor_identity()
    time.sleep(5)  # Allow Tor to build a new circuit
    print('[+] Your IP has been changed to:', ma_ip())

print('''\033[1;32;40m \n
                         _   _           _____          
                        | \ | | _____  _|_   _|__  _ __ 
                        |  \| |/ _ \ \/ / | |/ _ \| '__|
                        | |\  |  __/>  <  | | (_) | |   
                        |_| \_|\___/_/\_\ |_|\___/|_|   

                1.1                    
''')

print("\033[1;40;31m https://github.com/Stalin-143\n")
print("Nexulean")

os.system("service tor start")

time.sleep(3)
print("\033[1;32;40m Change your SOCKS to 127.0.0.1:9050 \n")

x = input("[+] Set time to change IP in seconds [default=60] >> ") or "60"
lin = input("[+] How many times do you want to change your IP? [0 = infinite] >> ") or "0"

try:
    x = int(x)
    lin = int(lin)

    if lin == 0:
        print("Starting infinite IP change. Press Ctrl+C to stop.")
        while True:
            try:
                change()
                time.sleep(x)
            except KeyboardInterrupt:
                print('\n[+] IP changer stopped.')
                break
    else:
        for _ in range(lin):
            change()
            time.sleep(x)

except ValueError:
    print("Invalid input. Please enter valid numbers.")
