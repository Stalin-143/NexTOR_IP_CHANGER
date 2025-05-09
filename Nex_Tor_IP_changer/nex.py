# -*- coding: utf-8 -*-
import time
import os
import subprocess
import random

try:
    import requests
    import stem
    from stem import Signal
    from stem.control import Controller
except Exception:
    print('[+] Installing required packages...')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    os.system('pip3 install stem')
    print('[!] Required packages installed')
    import requests
    import stem
    from stem import Signal
    from stem.control import Controller

# Check if Tor is installed
try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] tor is not installed!')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install tor -y', shell=True)
    print('[!] Tor is installed successfully')

os.system("clear")

# Function to check current IP through Tor
def get_current_ip():
    urls = [
        'http://checkip.amazonaws.com',
        'https://api.ipify.org',
        'https://ifconfig.me'
    ]
    
    url = random.choice(urls)
    try:
        get_ip = requests.get(
            url,
            proxies=dict(
                http='socks5://127.0.0.1:9050',
                https='socks5://127.0.0.1:9050'
            ),
            timeout=10
        )
        return get_ip.text.strip()
    except Exception as e:
        return f"Error getting IP: {str(e)}"

# Function to reset Tor identity - stronger method to change IP
def reset_tor_identity():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            time.sleep(controller.get_newnym_wait())
            return True
    except Exception as e:
        print(f"[!] Error changing Tor identity: {str(e)}")
        print("[!] Falling back to service restart method")
        return False

# Function to change IP address
def change_ip():
    print("[*] Requesting new Tor circuit...")
    
    current_ip = get_current_ip()
    
    # Try the stem controller method first (cleaner)
    if not reset_tor_identity():
        # If stem controller fails, restart the service
        os.system("sudo service tor restart")
        # Wait for Tor to fully restart
        time.sleep(5)
    
    new_ip = get_current_ip()
    
    # Verify IP has actually changed
    attempts = 0
    while new_ip == current_ip and attempts < 3:
        print("[!] IP didn't change, trying again...")
        if not reset_tor_identity():
            os.system("sudo service tor restart")
            time.sleep(5)
        new_ip = get_current_ip()
        attempts += 1
    
    if new_ip != current_ip:
        print(f'[+] IP successfully changed from {current_ip} to {new_ip}')
    else:
        print(f'[!] Failed to change IP after multiple attempts')
    
    return new_ip

# Setup Tor configuration
def setup_tor():
    print("[*] Setting up Tor...")
    
    # Create/modify torrc file to enable ControlPort
    torrc_path = "/etc/tor/torrc"
    backup_path = "/etc/tor/torrc.backup"
    
    # Backup original config if not already done
    if not os.path.exists(backup_path):
        os.system(f"sudo cp {torrc_path} {backup_path}")
    
    # Add necessary configurations
    control_port_config = """
# Added by ImprovedNexTOR
ControlPort 9051
CookieAuthentication 1
"""
    
    # Check if config already has these settings
    try:
        with open(torrc_path, 'r') as f:
            if "ControlPort 9051" not in f.read():
                print("[*] Updating Tor configuration...")
                os.system(f'echo "{control_port_config}" | sudo tee -a {torrc_path}')
    except:
        print("[!] Error reading torrc file. You may need to manually edit it.")
    
    # Start/restart Tor service
    os.system("sudo service tor restart")
    time.sleep(5)
    
    # Test connection
    try:
        test_ip = get_current_ip()
        print(f"[+] Tor is working! Current IP: {test_ip}")
        return True
    except Exception as e:
        print(f"[!] Error connecting to Tor: {str(e)}")
        return False

# ASCII Art
print('''\033[1;32;40m \n
                         *   *           _____          
                        | \ | | _____  *|*   *|*_  *_* 
                        |  \| |/ * \ \/ / | |/ * \| '__|
                        | |\  |  __/>  <  | | (_) | |   
                        |_| \_|\___/_/\_\ |_|\___/|_|   
                                                        
                        ImprovedNexTOR 1.2                    
''')
print("\033[1;40;31m https://github.com/Stalin-143\n")
print("Enhanced by Nexulean")

# Main program
if setup_tor():
    print("\033[1;32;40m")
    print("[+] Initial IP:", get_current_ip())
    print("[+] SOCKS proxy configured at 127.0.0.1:9050")
    
    try:
        change_interval = int(input("[+] Set time between IP changes in seconds [default=60] >> ") or "60")
        max_changes = input("[+] How many times do you want to change your IP? [0 for infinite] >> ") or "0"
        max_changes = int(max_changes)
        
        ip_history = []
        change_count = 0
        
        if max_changes == 0:
            print("[*] Starting infinite IP rotation. Press Ctrl+C to stop.")
            try:
                while True:
                    time.sleep(change_interval)
                    new_ip = change_ip()
                    ip_history.append(new_ip)
                    change_count += 1
                    print(f"[*] Total changes: {change_count}")
            except KeyboardInterrupt:
                print('\n[!] IP changer stopped by user.')
        else:
            print(f"[*] Starting {max_changes} IP rotations.")
            for i in range(max_changes):
                if i > 0:  # Skip the first wait
                    time.sleep(change_interval)
                new_ip = change_ip()
                ip_history.append(new_ip)
                print(f"[*] Change {i+1}/{max_changes} completed")
            
            print("\n[+] IP rotation complete!")
            
        # Summary
        if len(ip_history) > 1:
            print("\n[+] IP rotation summary:")
            print(f"[+] Total IP changes: {len(ip_history)}")
            print(f"[+] Unique IPs obtained: {len(set(ip_history))}")
            if len(ip_history) != len(set(ip_history)):
                print("[!] Some IPs were repeated during rotation.")
        
    except ValueError:
        print("[!] Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"[!] Error occurred: {str(e)}")
else:
    print("[!] Failed to set up Tor properly. Please check your installation.")
