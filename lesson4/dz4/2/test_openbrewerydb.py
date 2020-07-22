import pytest
import requests


class TestClassOpenbrewerydb:
    # 1 тест
    @pytest.mark.parametrize("url", ["san_diego", "san%20diego"])
    def test_list_breweries_by_city(self, url):
        res = requests.get(f'https://api.openbrewerydb.org/breweries?by_city={url}')
        js = res.json()
        assert res.status_code == 200
        for list in js:
            for k , v in list.items():
                if k == 'city':
                    assert v == 'San Diego'

    # 2 тест
    @pytest.mark.parametrize("url", ["cooper", "modern%20times"])
    def test_list_breweries_by_name(self, url):
        res = requests.get(f'https://api.openbrewerydb.org/breweries?by_name={url}')
        js = res.json()
        assert res.status_code == 200
        for list in js:
            for k, v in list.items():
                if url == 'cooper':
                    if k == 'name':
                        assert v.find("cooper")
                if url == 'modern%20times':
                    if k == 'name':
                        assert 'Modern Times' in v

    # 3 тест
    @pytest.mark.parametrize("url", ["by_state=ohio", "by_name=new_york", "by_name=new%20mexico"])
    def test_list_breweries_by_state(self, url):
        res = requests.get(f'https://api.openbrewerydb.org/breweries?{url}')
        js = res.json()
        assert res.status_code == 200
        for list in js:
            for k , v in list.items():
                if url == 'by_state=ohio':
                    if k == 'state':
                        assert v == 'Ohio'
                if url == 'by_name=new_york':
                    if k == 'name':
                        assert 'New York' in v
                if url == 'by_name=new%20mexico':
                    if k == 'name':
                        assert 'New Mexico' in v

    # 4 тест
    @pytest.mark.parametrize("url", ["44107", "44107-4020", "44107_4020"])
    def test_list_breweries_by_postal(self, url):
        res = requests.get(f'https://api.openbrewerydb.org/breweries?by_postal={url}')
        js = res.json()
        assert res.status_code == 200
        for list in js:
            for k, v in list.items():
                if k == 'postal_code':
                    assert url.replace('_', '-') in v

    # 5 тест
    @pytest.mark.parametrize("url", ["micro", "regional", "brewpub", "large",
                                     "planning", "bar", "contract", "proprietor"])
    def test_list_breweries_by_type(self, url):
        res = requests.get(f'https://api.openbrewerydb.org/breweries?by_type={url}')
        js = res.json()
        assert res.status_code == 200
        for list in js:
            for k, v in list.items():
                if k == 'brewery_type':
                    assert url in v