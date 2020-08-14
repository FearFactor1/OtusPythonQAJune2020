from lesson12.dz.page_objects.MainPage import MainPage
from lesson12.dz.page_objects.BasePage import BasePage
from lesson12.dz.page_objects.CatalogDesktops import CatalogDesktops
from lesson12.dz.page_objects.ProductId_49 import ProductId49
from lesson12.dz.page_objects.AccountLogin import AccountLogin
from lesson12.dz.page_objects.AdminPage import AdminPage


class TestClassOpencart:

    # 1 тест
    def test_main_page(self, browsers, url_browsers):
        browsers.get(url_browsers)
        assert browsers.title == 'Your Store'
        element_search = MainPage(browsers).element_search()
        element_search.send_keys("Apple Cinema 30")
        MainPage(browsers).button_search()
        assert browsers.current_url == \
               'https://demo.opencart.com/index.php?route=product/search&search=Apple%20Cinema%2030'
        assert browsers.title == 'Search - Apple Cinema 30'
        BasePage(browsers).return_home()
        assert browsers.title == 'Your Store'
        MainPage(browsers).button_dropdown()
        assert MainPage(browsers).navbar_in_home_page() == \
               'Desktops\nLaptops & Notebooks\nComponents\nTablets\nSoftware\nPhones & PDAs\nCameras\nMP3 Players'
        assert 'MacBook' in MainPage(browsers).featured_in_home_page()
        MainPage(browsers).bullet()
        assert MainPage(browsers).img_in_main_page() == \
                'https://demo.opencart.com/image/cache/catalog/demo/banners/MacBookAir-1140x380.jpg'
        browsers.quit()

    # 2 тест
    def test_catalog_desktops(self, browsers, url_browsers):
        browsers.get(f'{url_browsers}/index.php?route=product/category&path=20')
        assert browsers.title == 'Desktops'
        assert CatalogDesktops(browsers).img_thumbnail() == \
               'https://demo.opencart.com/image/cache/catalog/demo/compaq_presario-80x80.jpg'
        CatalogDesktops(browsers).refine_search_pc()
        assert browsers.current_url == 'https://demo.opencart.com/index.php?route=product/category&path=20_26'
        BasePage(browsers).return_desktop()
        assert browsers.title == 'Desktops'
        CatalogDesktops(browsers).refine_search_mac()
        assert browsers.current_url == 'https://demo.opencart.com/index.php?route=product/category&path=20_27'
        BasePage(browsers).return_desktop()
        assert browsers.title == 'Desktops'
        assert "Laptops & Notebooks (5)" in CatalogDesktops(browsers).desktop_colomn()
        browsers.quit()

    # 3 тест
    def test_product_id_49(self, browsers, url_browsers):
        browsers.get(f'{url_browsers}/index.php?route=product/product&path=57&product_id=49')
        assert browsers.title == 'Samsung Galaxy Tab 10.1'
        ProductId49(browsers).wish_in_product()
        assert ProductId49(browsers).alert_wish_login() == \
               'You must login or create an account to save Samsung Galaxy Tab 10.1 to your wish list!\n×'
        ProductId49(browsers).compare()
        assert ProductId49(browsers).alert_success() == \
               'Success: You have added Samsung Galaxy Tab 10.1 to your product comparison!\n×'
        assert ProductId49(browsers).thumbnail() == \
               'https://demo.opencart.com/image/cache/catalog/demo/samsung_tab_1-500x500.jpg'
        assert ProductId49(browsers).price_product()[8].text == '$241.99\nEx Tax: $199.99'
        browsers.quit()

    # 4 тест
    def test_account(self, browsers, url_browsers):
        browsers.get(f'{url_browsers}/index.php?route=account/login')
        assert browsers.title == 'Account Login'
        AccountLogin(browsers) \
            .login_user(email="fdgfd@gff.com", password="5555")
        assert browsers.title == 'My Account'
        AccountLogin(browsers) \
            .logout() \
            .continue_click()
        assert browsers.title == 'Your Store'
        MainPage(browsers) \
            .my_account() \
            .menu_my_account()
        AccountLogin(browsers) \
            .login_user(email="fdgfd@gff.com", password="5555") \
            .wish_list()
        assert browsers.title == 'My Wish List'
        assert AccountLogin(browsers).product_name_in_wish_list() \
               == 'My Wish List\nImage Product Name Model Stock Unit Price Action' \
                  '\nSamsung Galaxy Tab 10.1 SAM1 Pre-Order\n$199.99\nContinue'
        browsers.quit()

    # 5 тест
    def test_admin(self, browsers, url_browsers):
        browsers.get(f'{url_browsers}/admin/')
        AdminPage(browsers).button_login()
        assert browsers.title == 'Dashboard'
        AdminPage(browsers).button_logout()
        assert browsers.title == 'Administration'
        AdminPage(browsers) \
            .button_login() \
            .catalogs() \
            .products()
        assert browsers.title == "Products"
        assert "Apple Cinema 30" in AdminPage(browsers).table()
        browsers.quit()