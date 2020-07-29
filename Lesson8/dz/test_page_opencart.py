

class TestClassOpencart:

    # 1 тест
    def test_main_page(self, browser, url_browser):
        browser.get(url_browser)
        assert browser.title == 'OpenCart - Open Source Shopping Cart Solution'
        element = browser.find_element_by_css_selector("ul.nav.navbar-nav")
        browser.quit()