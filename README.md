![GitHub release (latest by date)](https://img.shields.io/github/v/release/cyb3rd3s/LogPars?style=for-the-badge) ![GitHub top language](https://img.shields.io/github/languages/top/cyb3rd3s/LogPars?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/cyb3rd3s/LogPars?style=for-the-badge)
# LogPars
Log Pars is a basic linux based log parser written in Python.
## Usage
If you are looking for one specific word:
```
logpars.py [error message you are looking for] [/var/log/TARGETLOG]
```
If you are looking for more than one word string, use **quotation marks**:
```
logpars.py ["error message you are looking for"] [/var/log/TARGETLOG]
```
## Example of output
```
kali@kali:~/LogPars$ sudo python3 logpars.py "password" /var/log/auth.log
                                                                                                                                                  
<=== Results ===>                                           
Found: Nov 20 12:46:00 kali lightdm: gkr-pam: stashed password to try later in open session
Found: Nov 20 12:48:05 kali sudo:     kali : 3 incorrect password attempts ; TTY=pts/0 ; PWD=/home/kali/LogPars ; USER=root ; COMMAND=/usr/bin/gedit exploit.py
Found: Nov 20 12:48:46 kali sudo:     kali : TTY=pts/0 ; PWD=/home/kali/LogPars ; USER=root ; COMMAND=/usr/bin/python logpars.py password /var/log/auth.log
Found: Nov 20 12:48:58 kali sudo:     kali : TTY=pts/0 ; PWD=/home/kali/LogPars ; USER=root ; COMMAND=/usr/bin/python3 logpars.py password /var/log/auth.log 
```
## Requirements

### Python 3.8
Whole script is written in Python 3.8., which is recommended for best functionality. Something might not work well in older versions. Python is free to download from [official website](https://www.python.org/downloads/) for all platforms.

## Help & issues
If you have any question, ideas or issues, you can report them through [Issues](https://github.com/cyb3rd3s/LogPars/issues).
