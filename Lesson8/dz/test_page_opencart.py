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
        assert browser.current_url == \
               'https://demo.opencart.com/index.php?route=product/search&search=Apple%20Cinema%2030'
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
        assert  img == 'https://demo.opencart.com/image/cache/catalog/demo/banners/MacBookAir-1140x380.jpg'
        browser.quit()

    # 2 тест
    def test_catalog_desktops(self, browser, url_browser):
        browser.get(f'{url_browser}/index.php?route=product/category&path=20')
        assert browser.title == 'Desktops'
        img_thumbnail = browser.find_element_by_css_selector("img.img-thumbnail").get_attribute("src")
        assert img_thumbnail == 'https://demo.opencart.com/image/cache/catalog/demo/compaq_presario-80x80.jpg'
        refine_search_pc = browser.find_element_by_link_text("PC (0)")
        refine_search_pc.click()
        assert browser.current_url == 'https://demo.opencart.com/index.php?route=product/category&path=20_26'
        return_desktop = browser.find_element_by_css_selector("ul.breadcrumb").find_element_by_link_text("Desktops")
        return_desktop.click()
        assert browser.title == 'Desktops'
        refine_search_mac = browser.find_element_by_link_text("Mac (1)")
        refine_search_mac.click()
        assert browser.current_url == 'https://demo.opencart.com/index.php?route=product/category&path=20_27'
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
        time.sleep(3)
        alert_login = browser.find_element_by_css_selector("div.alert.alert-success.alert-dismissible").text
        assert alert_login == \
               'You must login or create an account to save Samsung Galaxy Tab 10.1 to your wish list!\n×'
        compare = browser.find_element_by_css_selector("div.col-sm-4 > div > button > i.fa.fa-exchange")
        compare.click()
        time.sleep(3)
        alert_success = browser.find_element_by_css_selector("div.alert.alert-success.alert-dismissible").text
        assert 'Success: You have added Samsung Galaxy Tab 10.1 to your product comparison!\n×' == alert_success
        thumbnail = browser.find_element_by_css_selector("a.thumbnail").get_attribute("href")
        assert thumbnail == 'https://demo.opencart.com/image/cache/catalog/demo/samsung_tab_1-500x500.jpg'
        price = browser.find_elements_by_css_selector("ul.list-unstyled")[8].text
        assert price == '$241.99\nEx Tax: $199.99'
        browser.quit()

    # 4 тест
    def test_account(self, browser, url_browser):
        browser.get(f'{url_browser}/index.php?route=account/login')
        assert browser.title == 'Account Login'
        email = browser.find_element_by_css_selector("input[id=input-email]")
        email.send_keys("fdgfd@gff.com")
        password = browser.find_element_by_css_selector("input[id=input-password]")
        password.send_keys("5555")
        login = browser.find_element_by_css_selector("input[value=Login]")
        login.click()
        assert browser.title == 'My Account'
        logout = browser.find_element_by_link_text("Logout").click()
        continue_click = browser.find_element_by_link_text("Continue").click()
        assert browser.title == 'Your Store'
        my_account = browser.find_element_by_link_text("My Account")
        my_account.click()
        time.sleep(3)
        menu_acc = browser.find_element_by_link_text("Login")
        menu_acc.click()
        time.sleep(3)
        email = browser.find_element_by_css_selector("input[id=input-email]")
        email.send_keys("fdgfd@gff.com")
        password = browser.find_element_by_css_selector("input[id=input-password]")
        password.send_keys("5555")
        login = browser.find_element_by_css_selector("input[value=Login]")
        login.click()
        wish_list = browser.find_element_by_link_text("Wish List")
        wish_list.click()
        assert browser.title == 'My Wish List'
        product_name = browser.find_element_by_css_selector("div[id=content]").text
        assert product_name == 'My Wish List\nYour wish list is empty.\nContinue'
        browser.quit()

    # 5 тест
    def test_admin(self, browser, url_browser):
        browser.get(f'{url_browser}/admin/')
        assert browser.title == 'Administration'
        button_login = browser.find_element_by_css_selector("button.btn.btn-primary")
        button_login.click()
        assert browser.title == 'Dashboard'
        logout = browser.find_element_by_link_text("Logout")
        logout.click()
        assert browser.title == 'Administration'
        button_login = browser.find_element_by_css_selector("button.btn.btn-primary")
        button_login.click()
        catalogs = browser.find_element_by_css_selector("li[id=menu-catalog]")
        catalogs.click()
        time.sleep(3)
        products = browser.find_element_by_xpath("//a[contains(text(),'Products')]")
        products.click()
        assert browser.title == "Products"
        table = browser.find_element_by_css_selector("table.table.table-bordered.table-hover").text
        assert "Apple Cinema 30" in table
        browser.quit()