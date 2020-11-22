#!/usr/bin/env python3
# Name: LogPars
# Author: Roman Kulich @ 2020
# Version: v1.0.0

import argparse

TGREEN =  '\033[32m'
TWHITE = '\033[37m'
TRED = '\033[31m'
print(TGREEN + '''

.-.    .----.  .---. .----.  .--.  .----.  .----.
| |   /  {}  \/   __}| {}  }/ {} \ | {}  }{ {__  
| `--.\      /\  {_ }| .--'/  /\  \| .-. \.-._} }
`----' `----'  `---' `-'   `-'  `-'`-' `-'`----' 

''',TWHITE)
print(TGREEN + 'Usage: logpars.py "error message you are looking for" /var/log/TARGETLOG',TWHITE)

parser = argparse.ArgumentParser(description="")
parser.add_argument(dest='msg', help="logpars.py [error message] [target log]")
parser.add_argument(dest='log', help="logpars.py [error message] [target log]")
args = parser.parse_args()
message = (args.msg)
log = (args.log)
f = open(log)
lines = f.readlines()

print("")
print("<=== Results ===> ")
for line in lines:
    if line.__contains__(message):
        print("Found: " + TRED + (line.strip()),TWHITE)
