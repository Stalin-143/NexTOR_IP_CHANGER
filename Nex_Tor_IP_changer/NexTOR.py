# -*- coding: utf-8 -*-

import time
import os
import sys
import subprocess


def check_dependencies():
    """Check and report missing dependencies."""
    missing = []
    
    try:
        import requests
    except ImportError:
        missing.append("python3-requests")
    
    try:
        from stem import Signal
        from stem.control import Controller
    except ImportError:
        missing.append("python3-stem")
    
    try:
        subprocess.check_output('which tor', shell=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        missing.append("tor")
    
    if missing:
        print("[!] Missing dependencies:", ", ".join(missing))
        print("[!] Install with: sudo apt install", " ".join(missing))
        sys.exit(1)


def new_tor_identity():
    """Request a new Tor identity."""
    try:
        from stem import Signal
        from stem.control import Controller
        
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  # Uses default cookie auth
            controller.signal(Signal.NEWNYM)
            print('[*] Requested new identity from Tor')
    except Exception as e:
        print(f"[!] Failed to request new identity: {e}")


def ma_ip():
    """Get current IP through Tor SOCKS proxy."""
    import requests
    
    url = 'http://checkip.amazonaws.com'
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    get_ip = requests.get(url, proxies=proxies, timeout=10)
    return get_ip.text.strip()


def change():
    """Change to a new Tor exit IP."""
    new_tor_identity()
    time.sleep(5)  # Allow Tor to build a new circuit
    print('[+] Your IP has been changed to:', ma_ip())


def main():
    """Main entry point for the NexTOR IP changer."""
    # Check dependencies first
    check_dependencies()
    
    # Clear screen
    os.system("clear")
    
    # Print banner
    print(r'''
                         _   _           _____          
                        | \ | | _____  _|_   _|__  _ __ 
                        |  \| |/ _ \ \/ / | |/ _ \| '__|
                        | |\  |  __/>  <  | | (_) | |   
                        |_| \_|\___/_/\_\ |_|\___/|_|   

                1.1                    
''')
    
    print("\033[1;40;31m https://github.com/Stalin-143\n")
    print("Nexulean")
    
    # Start Tor service
    try:
        subprocess.check_call(['sudo', 'systemctl', 'start', 'tor'], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"[!] Failed to start tor service: {e}")
        print("[!] Make sure tor is installed and you have sudo access")
        sys.exit(1)
    
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


if __name__ == "__main__":
    main()
