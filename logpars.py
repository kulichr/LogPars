#!/usr/bin/env python3
# Name: LogPars
# Author: Roman Kulich @ 2020
# Version: v1.0.0

import argparse
import sys

TGREEN =  '\033[32m'
TWHITE = '\033[37m'
TRED = '\033[31m'
print(TGREEN + '''

.-.    .----.  .---. .----.  .--.  .----.  .----.
| |   /  {}  \/   __}| {}  }/ {} \ | {}  }{ {__  
| `--.\      /\  {_ }| .--'/  /\  \| .-. \.-._} }
`----' `----'  `---' `-'   `-'  `-'`-' `-'`----' 

''',TWHITE)

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="error message", dest='msg')
parser.add_argument("-l", help="log file", dest='log')
args = parser.parse_args()
message = args.msg
log = args.log

if log is None:
    print(TRED + "Missing logfile! ==>",TWHITE + TGREEN + "Usage: python3 logpars.py -m [error message] -l [target log]",TWHITE)
    print("")
    sys.exit()

f = open(log)
lines = f.readlines()

print("")
print("<=== Results ===> ")
for line in lines:
    if line.__contains__(message):
        print("Found: " + TRED + (line.strip()),TWHITE)
