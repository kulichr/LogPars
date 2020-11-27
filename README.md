![GitHub release (latest by date)](https://img.shields.io/github/v/release/cyb3rd3s/LogPars?style=for-the-badge) ![GitHub top language](https://img.shields.io/github/languages/top/cyb3rd3s/LogPars?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/cyb3rd3s/LogPars?style=for-the-badge)
# LogPars
Log Pars is a basic linux based log parser written in Python.
![Example of result](https://github.com/cyb3rd3s/cyb3rd3s/blob/main/logpars_example.png)
## Usage
If you are looking for one specific word:
```
python3 logpars.py [error message you are looking for] [/var/log/TARGETLOG]
```
If you are looking for more than one word string, use **quotation marks**:
```
python3 logpars.py ["error message you are looking for"] [/var/log/TARGETLOG]
```

## Requirements

### Python 3.8
Whole script is written in Python 3.8., which is recommended for best functionality. Something might not work well in older versions. Python is free to download from [official website](https://www.python.org/downloads/) for all platforms.

## Help & issues
If you have any question, ideas or issues, you can report them through [Issues](https://github.com/cyb3rd3s/LogPars/issues).
