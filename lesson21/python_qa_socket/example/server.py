import socket
import random

HOST = socket.gethostname()
PORT = random.randint(3000, 9999)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Биндимся на хост
    print("Биндимся на {}:{}".format(HOST, PORT))
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:

        conn.send("Hello, I am server!".encode("utf-8"))

        while True:

            data = conn.recv(1024)
            print("Recieved", data, "from", addr)

            if not data or data == b"close":
                print("Got", data, "and closed connection")
                conn.close()

            # Переворачиваем полученное сообщение и шлем обратно
            data = data.decode("utf-8")[::-1]
            conn.send(data.encode("utf-8"))

            # Выводим сообщение что отправили и куда
            print("Send", data, "to", addr)
