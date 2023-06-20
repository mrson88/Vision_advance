import socket
import sys
flag=False

clientTCP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=('localhost',6886)
try:
	clientTCP.connect(server_address)
	flag=True
except:
	print("server chua san sang")
	flag=False
while flag:
	#clientTCP.connect('localhost',6886)
	x= input('Your command: ')
	try:
		clientTCP.send(str(x).encode())
		print("vui long nhap gia tri")
		rec=clientTCP.recv(1024)
		print("gia tri nhan ve la: "+rec.decode())
	except:
		print("err")
		clientTCP.close()
		#Flag=False