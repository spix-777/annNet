#!/usr/local/bin/python3

import os, time, subprocess, random, sys, cursor
from progress.bar import Bar

class nameZ:
     def fake():
         faKename = []
         with open('data/lang', 'r') as target:
             faKename = target.readlines()
             x = subprocess.run(['sudo', 'scutil', '--set', 'HostName', random.choice(faKename)], capture_output=True)
             x = subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', random.choice(faKename)], capture_output=True)
             x = subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', random.choice(faKename)], capture_output=True)

class randomLIST:
    def ranVPN():
        if os.path.exists("data/randomLIST.py"):
            x = subprocess.run(['python3', 'data/randomLIST.py'], capture_output=True)
        else:
            print("The file does not exist")
            sys.exit(1)

class iFconFig:
    def ifCONFIG(Setting):
        x = subprocess.run(['sudo', 'ifconfig', Setting, 'down'], capture_output=True)
        time.sleep(sleep)
        x = subprocess.run(['sudo', 'ifconfig', Setting, 'up'], capture_output=True)
        time.sleep(sleep)

class spoofMac:
    def spoof_NeTworK(Setting):
        x = subprocess.run(['sudo', 'spoof-mac', 'randomize', Setting], capture_output=True)
        time.sleep(sleep)

class tOr:
    def  tOrserVice():
        x = subprocess.run(['brew', 'services', 'start', 'tor'], capture_output=True)


# --- SETTINGS ---
# Settings in a file "settings"
# If you are going to have some settings " See file settings "

def settingS():
    with open('settings', 'r') as target:
        count = 0
        listTaRget = target.readlines()
        for line in listTaRget:
            if line.find('#') == 0:
                pass
            elif line.find('#') != 0:
                if line > 'Setting' or 'sleep' or 'username' or 'password':
                    if count == 3:
                        strCount = line.rfind(' ')
                        Setting = line[strCount:]
                        Setting = Setting.strip()
                    elif count == 4:
                        strCount = line.rfind(' ')
                        sleep = int(line[strCount:])
                    elif count == 5:
                        strCount = line.rfind(' ')
                        username = line[strCount:]
                        username = username.strip()
                    elif count == 6:
                        strCount = line.rfind(' ')
                        password = line[strCount:]
                        password = password.strip()
                    else:
                        sys.exit(1)
            count += 1
    return Setting, sleep, username, password

Setting, sleep, username, password = settingS()

def SH():
    try:
        subprocess.Popen(['open /Applications/Tunnelblick.app'], shell=True)
        time.sleep(sleep)
        if os.path.exists("proton-run.sh"):
          subprocess.Popen(['sh','proton-run.sh'], stdin=None, stdout=None, stderr=None, shell=False)
          print('-------------------------------------------------------')
          print('OpenVPN / IKEv2 username:      '+username)
          print('OpenVPN / IKEv2 password:      '+password)
          print('-------------------------------------------------------')
          print('')
          input()
        else:
          print("The file does not exist")
          sys.exit(1)
    except KeyboardInterrupt:
        time.sleep(sleep)
        if os.path.exists("proton-run.sh"):
          os.remove("proton-run.sh")
        else:
          print("The file does not exist")
          sys.exit(1)
    return

if __name__ == '__main__':
    print('')
    print('''-------------------------------------------------------
|                    annNet                           |
|                 version 0.121                       |
-------------------------------------------------------''')
    cursor.hide()
    print()
    bar = Bar('   Processing', max=5)
    for i in range(1):
        nameZ.fake()
        bar.next()
        randomLIST.ranVPN()
        bar.next()
        iFconFig.ifCONFIG(Setting)
        bar.next()
        spoofMac.spoof_NeTworK(Setting)
        bar.next()
        tOr.tOrserVice()
        bar.next()
        time.sleep(0.6)
        bar.finish()

    print()
    SH()
    print()
    cursor.show()
