import socket

my_socket = socket.socket()
host = socket.gethostname()
address_and_port = (host, 8889)
my_socket.bind(address_and_port)

# https://docs.python.org/3/library/socket.html#socket.socket.listen
# Без дополнительной работы мы можем обрабатывать только одно соединение
# backlog - это размер очереди таких соединений
my_socket.listen(10)
