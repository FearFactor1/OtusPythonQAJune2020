import json


def test_check_log():
    with open("..\\..\\lesson19\\dz\\nginx_logs.txt", "r") as file:
        try:
            info = file.readlines(), "\n"
            for row in info:
                print(" ".join(row))
        except OSError:
            print('Не открывается файл!')