#!/usr/local/bin/python3

import sys, os

proxychains = "/usr/local/bin/proxychains4"
myip = "myip.py"

os.system(str(proxychains)+" python3 "+str(myip))

while True:
    try:
        cmd = input("#> ")
        os.system(str(proxychains)+" "+str(cmd))
    except KeyboardInterrupt:
        print()
        print("Bye! :)")
        sys.exit()
