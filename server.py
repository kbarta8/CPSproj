import socket                   # Import socket module

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
#s = socket.socket()             # Create a socket object
#host = ""   # Get local machine name
host = socket.gethostname()
addrs = socket.getaddrinfo("localhost", port, socket.AF_INET6, 0, socket.SOL_TCP)
entry0 = addrs[0]
sockaddr = entry0[-1]

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.bind(sockaddr)            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')


while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='TCPSERVER.py' #In the same folder or path is this file running must the file you want to tranfser to be
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()
