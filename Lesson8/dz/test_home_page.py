

def test_home_page(browser, url_browser):
    browser.get(url_browser)
    assert browser.title == 'OpenCart - Open Source Shopping Cart Solution'
    browser.quit()