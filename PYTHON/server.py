import socket

def mpm():
    host = '127.0.0.1'
    port = 6000
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    print('Waiting for connection...')
    c,addr = s.accept()
    print('Connection Established!')
    print('Client Address: ',addr)
    print()
    while True:
        try:
            data = c.recv(1024)
            msg = data.decode('ascii')
            print('Client: ',msg)
            x = input('Enter the message: ')
            y = x.encode('ascii')
            c.send(y)
        except KeyboardInterrupt:
            print()
            print('Connection Break!')
            break 

            
mpm()