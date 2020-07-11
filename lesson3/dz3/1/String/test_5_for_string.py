import pytest




class TestClassString:

    # 1 тест
    @pytest.mark.parametrize("count", ['email', 'user', 'привет'])
    def test_count_string(self, count):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            counts = f.count(count)
            print(counts)


    # 2 тест
    def test_upper_string(self):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            up = f.upper()
            print(up)


    # 3 тест
    def test_split_string(self):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            sp = f.split()
            print(sp)


    # 4 тест
    def test_join_string(self):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            j = " ".join(f)
            print(j)


    # 5 тест
    def test_replace_string(self):
        with open('../String/datadz.xml', 'r') as file:
            f = file.read()
            rp = f.replace('<', ' ')
            print(rp)