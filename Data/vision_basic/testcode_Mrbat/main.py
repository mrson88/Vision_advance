import socket
import sys
flag=False
ip_server ='localhost'
port=6886
server_TCP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=('localhost',6886)
try:
	server_TCP.bind(server_address)
	server_TCP.listen(10)
	print("server da san sang")
	flag=True
except:
	print("server chua san sang")
	flag=False
while flag:
	#clientTCP.connect('localhost',6886)
	client_socket, client_address= server_TCP.accept()
	data= client_socket.recv(1024).decode('UTF-8')
	print("gia tri nhan ve la: " + data)
	if data == "hi iam robot":
			makeData="hi iam robot"
	try:
		client_socket.send(makeData.encode())
	except:
		print("err")
		client_socket.close()
		#Flag=False