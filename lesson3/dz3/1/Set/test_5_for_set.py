import pytest
import json


class TestClassSet:

    # 1 тест
    @pytest.mark.parametrize("status", ['Играют на выезде', 'играют дома', 'играют в лиги чемпионов'])
    def test_add_set(self, status):
        with open("../Set/datadz.json", "r") as f:
            clubs = json.loads(f.read())
            info_clubs = clubs['clubs']
            for setu in info_clubs:
                sets = set(setu)
                sets.add(status)
                assert status in sets
                print(sets)


    # 2 тест
    def test_discard_set(self):
        with open("../Set/datadz.json", "r") as f:
            clubs = json.loads(f.read())
            info_clubs = clubs['clubs']
            for setu in info_clubs:
                sets = set(setu)
                sets.discard('name')
                assert 'name' not in sets
                print(sets)


    # 3 тест
    def test_copy_set(self):
        with open("../Set/datadz.json", "r") as f:
            clubs = json.loads(f.read())
            info_clubs = clubs['clubs']
            for setu in info_clubs:
                sets = set(setu)
                cop = sets.copy()
                assert cop == sets
                print(cop)


    # 4 тест
    def test_len_set(self):
        with open("../Set/datadz.json", "r") as f:
            clubs = json.loads(f.read())
            info_clubs = clubs['clubs']
            for setu in info_clubs:
                sets = set(setu)
                lens = len(sets)
                assert lens == 5
                print(lens)


    # 5 тест
    def test_frozenset_set(self):
        with open("../Set/datadz.json", "r") as f:
            clubs = json.loads(f.read())
            info_clubs = clubs['clubs']
            for setu in info_clubs:
                sets = set(setu)
                frozensets = frozenset(sets)
                assert "email" in frozensets
                print(frozensets)
