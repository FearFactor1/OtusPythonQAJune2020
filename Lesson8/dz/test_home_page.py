

def test_home_page(browser, url_browser):
    browser.get(url_browser)
    assert browser.title == 'Your Store'
    browser.quit()