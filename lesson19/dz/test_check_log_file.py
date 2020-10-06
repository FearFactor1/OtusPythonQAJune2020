import re
from collections import Counter
import json


def test_check_log():
    with open("..\\..\\lesson19\\dz\\nginx_logs.txt", "r") as file:
        try:
            info = file.readlines(), "\n"
            for row in info:
                get = re.findall('GET', str(row))
                head = re.findall('HEAD', str(row))
                times = re.findall('(.*?) "-"', str(row))
                err_clients = re.findall('4\d\d', str(row))
                err_serv = re.findall('5\d\d', str(row))
                sb = []
                for i in times:
                    if i == "":
                        continue
                    sa = str(i).split()
                    s = sb.append(sa[-1])
                ba = sorted(sb, reverse=True)
                break
        except OSError:
            print('Не открывается файл!')
    with open("..\\..\\lesson19\\dz\\statistics.json", "w") as f:
        try:
            i = 1
            sum = [json.dumps(len(row), indent=4)]
            sumg = [json.dumps(len(get), indent=4)]
            sumh = [json.dumps(len(head), indent=4)]
            long_t = [json.dumps(ba[0:10], indent=4)]
            cl_e = [json.dumps(err_clients[0:10], indent=4)]
            sr_e = [json.dumps(err_serv[0:10], indent=4)]
            for k, j, s, l, ce, se in zip(sum, sumg, sumh, long_t, cl_e, sr_e):
                f.write(f'Общее количество выполненных запросов - {k}' + '\n')
                f.write(f'Количество запросов по типу: GET - {j}' + '\n')
                f.write(f'Количество запросов по типу: HEAD - {s}' + '\n')
                f.write(f'топ 10 самых долгих запросов - {l}' + '\n')
                f.write(f'топ 10 запросов, которые завершились клиентской ошибкой - {ce}' + '\n')
                f.write(f'топ 10 запросов, которые завершились ошибкой со стороны сервера - {se}' + '\n')
                for ip, count in Counter(row).most_common(10):
                    f.write(f'топ 10 IP адресов, с которых были сделаны запросы - {ip}' + '\n')
        except OSError:
            print('Не открывается файл!')