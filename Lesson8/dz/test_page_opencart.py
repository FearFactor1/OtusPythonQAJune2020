import time


class TestClassOpencart:

    # 1 тест
    def test_main_page(self, browser, url_browser):
        browser.get(url_browser)
        assert browser.title == 'Your Store'
        element_search = browser.find_element_by_css_selector("input.form-control.input-lg")
        element_search.send_keys("Apple Cinema 30")
        button_search = browser.find_element_by_css_selector("button.btn.btn-default.btn-lg")
        button_search.click()
        assert browser.current_url == 'http://localhost/index.php?route=product/search&search=Apple%20Cinema%2030'
        assert browser.title == 'Search - Apple Cinema 30'
        retun_home = browser.find_element_by_link_text("Your Store")
        retun_home.click()
        assert browser.title == 'Your Store'
        button_dropdown = browser.find_element_by_css_selector(
            "button.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle")
        button_dropdown.click()
        navbar = browser.find_element_by_css_selector("div.collapse.navbar-collapse.navbar-ex1-collapse").text
        assert navbar == \
               'Desktops\nLaptops & Notebooks\nComponents\nTablets\nSoftware\nPhones & PDAs\nCameras\nMP3 Players'
        Featured = browser.find_element_by_css_selector("div.product-thumb.transition").text
        assert 'MacBook' in Featured
        bullet = browser.find_element_by_css_selector(
            "span.swiper-pagination-bullet.swiper-pagination-bullet-active")
        bullet.click()
        img = browser.find_element_by_tag_name("img").get_attribute("src")
        assert  img == 'http://localhost/image/cache/catalog/demo/banners/MacBookAir-1140x380.jpg'
        browser.quit()

    # 2 тест
    def test_catalog_desktops(self, browser, url_browser):
        browser.get(f'{url_browser}/index.php?route=product/category&path=20')
        assert browser.title == 'Desktops'
        img_thumbnail = browser.find_element_by_css_selector("img.img-thumbnail").get_attribute("src")
        assert img_thumbnail == 'http://localhost/image/cache/catalog/demo/compaq_presario-80x80.jpg'
        refine_search_pc = browser.find_element_by_link_text("PC (0)")
        refine_search_pc.click()
        assert browser.current_url == 'http://localhost/index.php?route=product/category&path=20_26'
        return_desktop = browser.find_element_by_css_selector("ul.breadcrumb").find_element_by_link_text("Desktops")
        return_desktop.click()
        assert browser.title == 'Desktops'
        refine_search_mac = browser.find_element_by_link_text("Mac (1)")
        refine_search_mac.click()
        assert browser.current_url == 'http://localhost/index.php?route=product/category&path=20_27'
        return_desktop = browser.find_element_by_css_selector("ul.breadcrumb").find_element_by_link_text("Desktops")
        return_desktop.click()
        assert browser.title == 'Desktops'
        desktop_colomn = browser.find_element_by_css_selector("div.list-group").text
        assert "Laptops & Notebooks (5)" in desktop_colomn
        browser.quit()

    # 3 тест
    def test_product_id_49(self, browser, url_browser):
        browser.get(f'{url_browser}/index.php?route=product/product&path=57&product_id=49')
        assert browser.title == 'Samsung Galaxy Tab 10.1'
        wish = browser.find_element_by_css_selector("div.col-sm-4 > div > button > i.fa.fa-heart")
        wish.click()
        time.sleep(7)
        alert_login = browser.find_element_by_css_selector("div.alert.alert-success.alert-dismissible").text
        assert alert_login == \
               'You must login or create an account to save Samsung Galaxy Tab 10.1 to your wish list!\n×'
        compare = browser.find_element_by_css_selector("div.col-sm-4 > div > button > i.fa.fa-exchange")
        compare.click()
        time.sleep(7)
        alert_success = browser.find_element_by_css_selector("div.alert.alert-success.alert-dismissible").text
        assert 'Success: You have added Samsung Galaxy Tab 10.1 to your product comparison!\n×' == alert_success
        browser.quit()