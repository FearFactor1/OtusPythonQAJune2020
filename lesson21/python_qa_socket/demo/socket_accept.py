import socket

my_socket = socket.socket()
host = socket.gethostname()
address_and_port = (host, 8871)
my_socket.bind(address_and_port)
print("Started socket on", address_and_port)
my_socket.listen(10)

# https://docs.python.org/3/library/socket.html#socket.socket.accept
conn, addr = my_socket.accept()

# При подключении возвращает параметры соединения и адрес клиента
print(conn, addr)

my_socket.close()
