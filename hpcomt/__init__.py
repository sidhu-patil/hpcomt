# Created By Sidhu Patil
# Specailly For Detect Android OS 

import subprocess
import platform

def __init__():
    """\nReturns The System/OS Name, E.g. 'Android', 'Linux', 'Windows' or 'Java' , Etc .\n
Special Thing In This Module It Can Be Detect Android OS\n"""
    non = ""


def Name():
    """\nReturns The System/OS Name, E.g. 'Android', 'Linux', 'Windows' or 'Java' , Etc .\n
Special Thing In This Module It Can Be Detect Android OS\n"""
    check = platform.system()
    check1 = check.upper()
    if "LINUX" in check1: 
        try:
            path = subprocess.check_output('which python3', shell=True)
            if "com.termux" in str(path):
                check = "Android"
            else:  
                check = "Linux"          
        except:
            pass
    return check      
