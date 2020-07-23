import pytest
import requests


class TestClassJsonplaceholder:
    # 1 тест
    def test_100_posts(self):
        res = requests.get(f'https://jsonplaceholder.typicode.com/posts')
        js = res.json()
        i = 0
        dicid = {}
        assert js != []
        for list in js:
            for k, v in list.items():
                if k == 'id':
                    dicid = k
                    i += 1
        assert i == 100

    def test_100_posts_1_comments(self):
        res = requests.get(f'https://jsonplaceholder.typicode.com/posts/1/comments')
        js = res.json()
        i = 0
        dicid = {}
        assert js != []
        for list in js:
            for k, v in list.items():
                if k == 'postId':
                    assert v == 1

    # 2 тест
    def test_500_comments(self):
        res = requests.get(f'https://jsonplaceholder.typicode.com/comments')
        js = res.json()
        i = 0
        dicid = {}
        assert js != []
        for list in js:
            for k, v in list.items():
                if k == 'id':
                    dicid = k
                    i += 1
        assert i == 500

    def test_500_comments_postId(self):
        res = requests.get(f'https://jsonplaceholder.typicode.com/posts/1/comments')
        js = res.json()
        i = 0
        dicid = {}
        assert js != []
        for list in js:
            for k, v in list.items():
                if k == 'postId':
                    assert v == 1

    # 3 тест
    def test_100_albums(self):
        res = requests.get(f'https://jsonplaceholder.typicode.com/albums')
        js = res.json()
        i = 0
        dicid = {}
        assert js != []
        for list in js:
            for k, v in list.items():
                if k == 'id':
                    dicid = k
                    i += 1
        assert i == 100

    # 4 тест
    def test_5000_photos(self):
        res = requests.get(f'https://jsonplaceholder.typicode.com/photos')
        js = res.json()
        i = 0
        dicid = {}
        assert js != []
        for list in js:
            for k, v in list.items():
                if k == 'id':
                    dicid = k
                    i += 1
        assert i == 5000

    # 5 тест
    def test_200_todos(self):
        res = requests.get(f'https://jsonplaceholder.typicode.com/todos')
        js = res.json()
        i = 0
        dicid = {}
        assert js != []
        for list in js:
            for k, v in list.items():
                if k == 'id':
                    dicid = k
                    i += 1
        assert i == 200