import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 NexTOR.py')
    run('mkdir /usr/share/Nex')
    run('cp NexTOR.py /usr/share/Nex/NexTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/Nex/NexTOR.py "$@"')
    with open('/usr/bin/Nex','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/Nex & chmod +x /usr/share/Nex/NexTOR.py')
    print('''\n\ncongratulation Nex Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42mNex\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/Nex ')
    run('rm /usr/bin/Nex ')
    print('[!] now Nex Tor Ip changer  has been removed successfully')
