import json
from csv import DictReader


def test_creat_json():
    with open("../2/users.json", "r") as file:
        info = json.load(file)
        rows = {}
        dic = {}
        i = 1
        for name in info:
            n = name.get("name")
            g = name.get("gender")
            a = name.get("address")
            dic[i] = n, g , a
            i += 1
        print(dic)
    with open("../2/books.csv", "r") as file:
        i = 1
        reader = DictReader(file)
        for row in reader:
            rows[i] = row
            i += 1
        print(rows)
    with open("../2/example.json", "w") as f:
        i = 1
        s = [json.dumps(dic, indent=4)]
        sd = [json.dumps(rows, indent=4)]
        for k, j in zip(s, sd):
            f.write(k)
            f.write(j)
            print(k, j)