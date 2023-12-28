import socket

def mpm():
    host = '127.0.0.1'
    port = 6000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    print('Connection Established!')
    print()
    while True:
        try:
            x = input('Enter the message: ')
            y = x.encode('ascii')
            s.send(y)
            data = s.recv(1024)
            msg = data.decode('ascii')
            print('Server: ',msg)
        except KeyboardInterrupt:
            print()
            print('Connection Break!')
            s.send('Connection Stopped from the client side!')
            break

mpm()