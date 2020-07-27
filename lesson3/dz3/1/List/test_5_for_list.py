import pytest


class TestClassList:

    # 1 тест
    @pytest.mark.parametrize("info", [1, 2, 3])
    def test_append_list(self, info):
        with open("../List/datadz.csv", "r") as file:
            for line in file.readlines():
                sp = line.split("\n")
                sp.append(info)
                assert info in sp
                print(sp, end='')


    # 2 тест
    @pytest.mark.parametrize("champions", ['три раза чемпион', 'два раза чемпион', 'один раз чемпион'])
    def test_insert_item_in_list(self, champions):
        with open("../List/datadz.csv", "r") as file:
            for line in file.readlines():
                sp = line.split("\n")
                sp.insert(-1, champions)
                assert champions in sp
                print(sp, end='')


    # 3 тест
    def test_pop_list(self):
        with open("../List/datadz.csv", "r") as file:
            for line in file.readlines():
                sp = line.split("\n")
                sp.pop(0)
                assert 'club1,milan,city,milan' not in sp
                print(sp, end='')


    # 4 тест
    def test_count_list(self):
        with open("../List/datadz.csv", "r") as file:
            for line in file.readlines():
                sp = line.split("\n")
                club = sp.count('club1,milan,city,milan')
                assert sp != 0
                print(sp, end='')
                print(club, end='')


    #5 тест
    def test_clear_list(self):
        with open("../List/datadz.csv", "r") as file:
            for line in file.readlines():
                sp = line.split("\n")
                sort = sp.clear()
                assert sp == []
                print(sp, end='')
                print(sort, end='')
