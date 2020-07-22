import pytest
import requests


class TestClassJsonplaceholder:
    # 1 тест
    @pytest.mark.parametrize("resource", ["posts", "posts/1/comments"])
    def test_100_posts(self, resource):
        res = requests.get(f'https://jsonplaceholder.typicode.com/{resource}')
        js = res.json()
        i = 0
        dicid = {}
        if resource == "posts":
            for list in js:
                for k, v in list.items():
                    if k == 'id':
                        dicid = k
                        i += 1
            assert i == 100
            print(i)
        if resource == "posts/1/comments":
            for list in js:
                for k, v in list.items():
                    if k == 'postId':
                        assert v == 1

    # 2 тест
    @pytest.mark.parametrize("resource", ["comments", "comments?postId=1"])
    def test_500_comments(self, resource):
        res = requests.get(f'https://jsonplaceholder.typicode.com/{resource}')
        js = res.json()
        i = 0
        dicid = {}
        if resource == "comments":
            for list in js:
                for k, v in list.items():
                    if k == 'id':
                        dicid = k
                        i += 1
            assert i == 500
            print(i)
        if resource == "comments?postId=1":
            for list in js:
                for k, v in list.items():
                    if k == 'postId':
                        assert v == 1

    # 3 тест
    @pytest.mark.parametrize("resource", ["albums"])
    def test_100_albums(self, resource):
        res = requests.get(f'https://jsonplaceholder.typicode.com/{resource}')
        js = res.json()
        i = 0
        dicid = {}
        for list in js:
            for k, v in list.items():
                if k == 'id':
                    dicid = k
                    i += 1
        assert i == 100
        print(i)

    # 4 тест
    @pytest.mark.parametrize("resource", ["photos"])
    def test_5000_photos(self, resource):
        res = requests.get(f'https://jsonplaceholder.typicode.com/{resource}')
        js = res.json()
        i = 0
        dicid = {}
        for list in js:
            for k, v in list.items():
                if k == 'id':
                    dicid = k
                    i += 1
        assert i == 5000
        print(i)

    # 5 тест
    @pytest.mark.parametrize("resource", ["todos"])
    def test_200_todos(self, resource):
        res = requests.get(f'https://jsonplaceholder.typicode.com/{resource}')
        js = res.json()
        i = 0
        dicid = {}
        for list in js:
            for k, v in list.items():
                if k == 'id':
                    dicid = k
                    i += 1
        assert i == 200
        print(i)