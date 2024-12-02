import os
import subprocess

choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':
    try:
        check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
        if str('install ok installed') in str(check_pip3):
            pass
    except subprocess.CalledProcessError:
        print('[+] pip3 not installed')
        subprocess.check_output('sudo apt update',shell=True)
        subprocess.check_output('sudo apt install python3-pip -y', shell=True)
        print('[!] pip3 installed succesfully')

    try:

        import requests
    except Exception:
        print('[+] python3 requests is not installed')
        os.system('pip3 install requests')
        os.system('pip3 install requests[socks]')
        print('[!] python3 requests is installed ')
    try:

        check_tor = subprocess.check_output('which tor', shell=True)
    except subprocess.CalledProcessError:

        print('[+] tor is not installed !')
        subprocess.check_output('sudo apt update',shell=True)
        subprocess.check_output('sudo apt install tor -y',shell=True)
        print('[!] tor is installed succesfully ')

    run('chmod 777 aparatlike.py')
    run('mkdir /usr/share/aparatlike')
    run('cp aparatlike.py /usr/share/aparatlike/aparatlike.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aparatlike/aparatlike.py "$@"')
    with open('/usr/bin/aparatlike','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aparatlike & chmod +x /usr/share/aparatlike/aparatlike.py')
    print('''\n\ncongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maparatlike\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aparatlike ')
    run('rm /usr/bin/aparatlike ')
    print('[!] now aparatlike has been removed successfully')
