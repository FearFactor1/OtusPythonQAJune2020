import socket

default_socket = socket.socket()
address_and_port = ('localhost', 8888)

# Можем биндить на порты выше 1023
default_socket.bind(address_and_port)
print("Socket 1 binded on", address_and_port)

my_socket = socket.socket()
host = socket.gethostname()
address_and_port = (host, 8889)

# Так же можно воспользоваться встроенной функцией
my_socket.bind(address_and_port)
print("Socket 2 binded on", address_and_port)

my_socket.close()
default_socket.close()
