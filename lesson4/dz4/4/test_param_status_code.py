

def test_url_status(url_status, method_get, method_status_code):
    response = method_get(url_status)
    assert response.status_code == method_status_code