import socket                   # Import socket module

from Crypto.Cipher import AES   #https://pypi.org/project/pycrypto/

port = 7778                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='mytext.txt'
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    f = open(filename,'rb')
    l = obj.encrypt(f.read(1024))
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    q = ('Thank you for connecting')
    b3 = bytes(q, encoding = 'utf-8')
    #conn.send(b3)
    conn.close()
