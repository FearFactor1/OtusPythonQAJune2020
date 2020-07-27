import pytest


class TestClassDictionary:

    # 1 тест
    @pytest.mark.parametrize("words1", ['как и везде'])
    @pytest.mark.parametrize("words2", ['знают все'])
    def test_add_in_dictionary(self, words1, words2):
        with open("../Dictionary/datadz.txt", "r") as file:
            words = [i.strip().lower() for i in file.read().split()]
            dword = dict(zip(words[:-1], words[1:]))
            dword[words1] = words2
            assert words1 in dword
            print(dword, end='')


    # 2 тест
    def test_pop_in_dictionary(self):
        with open("../Dictionary/datadz.txt", "r") as file:
            words = [i.strip().lower() for i in file.read().split()]
            dword = dict(zip(words[:-1], words[1:]))
            pops = dword.pop("the")
            assert "the" not in dword
            print(pops, end='')


    # 3 тест
    def test_clear_dictionary(self):
        with open("../Dictionary/datadz.txt", "r") as file:
            words = [i.strip().lower() for i in file.read().split()]
            dword = dict(zip(words[:-1], words[1:]))
            dword.clear()
            assert dword == {}
            print(dword)


    # 4 тест
    def test_get_dictionary(self):
        with open("../Dictionary/datadz.txt", "r") as file:
            words = [i.strip().lower() for i in file.read().split()]
            dword = dict(zip(words[:-1], words[1:]))
            gets = dword.get("to")
            assert gets == "support"
            print(gets)


    # 5 тест
    def test_len_dictionary(self):
        with open("../Dictionary/datadz.txt", "r") as file:
            words = [i.strip().lower() for i in file.read().split()]
            dword = dict(zip(words[:-1], words[1:]))
            lens = len(dword)
            assert lens == 29
            print(lens)

