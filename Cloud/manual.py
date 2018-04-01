import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.31.54', 6102)) 

client_socket.send('ON')
client_socket.recv(1024)

client_socket.close()
