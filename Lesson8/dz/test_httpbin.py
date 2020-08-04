import requests


def test_httpbin():
        res = requests.get('http://httpbin.org/redirect/1')
        assert res.status_code == 404
        assert res.apparent_encoding == None
        assert res.encoding == 'utf-8'
        assert res.ok == False
        assert res.reason == 'Not Found'
        print(res)