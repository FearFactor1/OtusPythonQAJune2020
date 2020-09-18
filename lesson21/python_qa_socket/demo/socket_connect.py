import socket

my_socket = socket.socket()
host = socket.gethostname()
address_and_port = (host, 8889)

# https://docs.python.org/3/library/socket.html#socket.socket.connect
my_socket.connect(address_and_port)

my_socket.close()
