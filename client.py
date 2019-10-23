import socket                   # Import socket module
from Crypto.Cipher import AES   #https://pypi.org/project/pycrypto/


s = socket.socket()             # Create a socket object
host = "10.138.21.141"
port = 7778                 # Reserve a port for your service.

s.connect((host, port))
l="Hello server!"
b1 = bytes(l)
s.send(b1)

with open('received_file', 'wb') as f:
	print ('file opened')
    #if True:
	print('receiving data...')
	obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
	data = obj2.decrypt(s.recv(1024))
	print('data=%s', (data))
	f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
