#!/usr/local/bin/python3

import os, sys, time, subprocess

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

x = subprocess.run(['sudo', 'pkill', 'sh', 'proton-run.sh'], capture_output=True)
time.sleep(1)
x = subprocess.run(['sudo', 'pkill', 'sh'], capture_output=True)
time.sleep(1)
x = subprocess.run(['sudo', 'pkill', '-f', 'Tunnelblick'], capture_output=True)
time.sleep(1)
x = subprocess.run(['sudo', 'spoof-mac', 'randomize', Setting], capture_output=True)
time.sleep(1)
x = subprocess.run(['brew', 'services', 'stop', 'tor'], capture_output=True)
time.sleep(1)
try:
    os.remove('proton-run.sh')
except:
    pass
