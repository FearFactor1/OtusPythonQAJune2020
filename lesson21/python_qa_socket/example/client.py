import socket
import sys

HOST = socket.gethostname()
PORT = int(sys.argv[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    print("Полдключаюсь к {}:{}".format(HOST, PORT))
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(repr(data))

    while True:
        data_to_send = input("Давайте отправим: ")

        if data_to_send == 'close':
            s.send(bytes(data_to_send.strip(), "utf-8"))
            print("Закрываем соединение")
            break

        s.send(bytes(data_to_send.strip(), "utf-8"))
        data = s.recv(1024)

        print('Получено:', repr(data))
