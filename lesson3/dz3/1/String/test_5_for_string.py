import pytest


class TestClassString:

    # 1 тест
    @pytest.mark.parametrize("count", ['email', 'user', 'привет'])
    def test_count_string(self, count):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            counts = f.count(count)
            assert counts != '0'
            print(counts)


    # 2 тест
    def test_upper_string(self):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            up = f.upper()
            assert 'MOSCOW' in up
            print(up)


    # 3 тест
    def test_split_string(self):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            sp = f.split()
            assert len(sp) == 24
            print(sp)


    # 4 тест
    def test_join_string(self):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            j = " ".join(f)
            assert " M o s c o w " in j
            print(j)


    # 5 тест
    def test_replace_string(self):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            rp = f.replace('<', ' ')
            assert '<' not in rp
            print(rp)