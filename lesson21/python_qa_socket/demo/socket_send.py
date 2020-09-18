import socket

my_socket = socket.socket()
host = socket.gethostname()
address_and_port = (host, 8889)

my_socket.connect(address_and_port)

# https://docs.python.org/3/library/socket.html#socket.socket.send
data_amount = my_socket.send(b"Hello, socket!")
print("Send", data_amount, "bytes")

my_socket.close()
