import socket

my_socket = socket.socket()
host = socket.gethostname()

address_and_port = (host, 8889)
my_socket.bind(address_and_port)

print("Started socket on", address_and_port)
my_socket.listen(10)

conn, addr = my_socket.accept()
print("Got connection", conn, addr)

# Получаем данные из соединения
data = conn.recv(1024)
print("Got data", data)

# Попробуем получить что-то более интересное
# conn.send("HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: text/html\n\n <h1>Hello from OTUS!</h1>".encode("utf-8"))

my_socket.close()
