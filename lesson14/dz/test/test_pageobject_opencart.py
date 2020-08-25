from lesson14.dz.page_objects.MainPage import MainPage
from lesson14.dz.page_objects.BasePage import BasePage
from lesson14.dz.page_objects.CatalogDesktops import CatalogDesktops
from lesson14.dz.page_objects.ProductId_49 import ProductId49
from lesson14.dz.page_objects.AccountLogin import AccountLogin
from lesson14.dz.page_objects.AdminPage import AdminPage


class TestClassOpencart:

    # 1 тест
    def test_main_page(self, browser_se, url_browser_se):
        browser_se.get(url_browser_se)
        assert browser_se.title == 'Your Store'
        element_search = MainPage(browser_se).element_search()
        element_search.send_keys("Apple Cinema 30")
        MainPage(browser_se).button_search()
        assert browser_se.current_url == \
               'https://demo.opencart.com/index.php?route=product/search&search=Apple%20Cinema%2030'
        assert browser_se.title == 'Search - Apple Cinema 30'
        BasePage(browser_se).return_home()
        assert browser_se.title == 'Your Store'
        MainPage(browser_se).button_dropdown()
        assert MainPage(browser_se).navbar_in_home_page() == \
               'Desktops\nLaptops & Notebooks\nComponents\nTablets\nSoftware\nPhones & PDAs\nCameras\nMP3 Players'
        assert 'MacBook' in MainPage(browser_se).featured_in_home_page()
        MainPage(browser_se).bullet()
        assert MainPage(browser_se).img_in_main_page() == \
                'https://demo.opencart.com/image/cache/catalog/demo/banners/MacBookAir-1140x380.jpg'

    # 2 тест
    def test_catalog_desktops(self, browser_se, url_browser_se):
        browser_se.get(f'{url_browser_se}/index.php?route=product/category&path=20')
        assert browser_se.title == 'Desktops'
        assert CatalogDesktops(browser_se).img_thumbnail() == \
               'https://demo.opencart.com/image/cache/catalog/demo/compaq_presario-80x80.jpg'
        CatalogDesktops(browser_se).refine_search_pc()
        assert browser_se.current_url == 'https://demo.opencart.com/index.php?route=product/category&path=20_26'
        BasePage(browser_se).return_desktop()
        assert browser_se.title == 'Desktops'
        CatalogDesktops(browser_se).refine_search_mac()
        assert browser_se.current_url == 'https://demo.opencart.com/index.php?route=product/category&path=20_27'
        BasePage(browser_se).return_desktop()
        assert browser_se.title == 'Desktops'
        assert "Laptops & Notebooks (5)" in CatalogDesktops(browser_se).desktop_colomn()

    # 3 тест
    def test_product_id_49(self, browser_se, url_browser_se):
        browser_se.get(f'{url_browser_se}/index.php?route=product/product&path=57&product_id=49')
        assert browser_se.title == 'Samsung Galaxy Tab 10.1'
        ProductId49(browser_se).wish_in_product()
        assert ProductId49(browser_se).alert_wish_login() == \
               'You must login or create an account to save Samsung Galaxy Tab 10.1 to your wish list!\n×'
        ProductId49(browser_se).compare()
        assert ProductId49(browser_se).alert_success() == \
               'Success: You have added Samsung Galaxy Tab 10.1 to your product comparison!\n×'
        assert ProductId49(browser_se).thumbnail() == \
               'https://demo.opencart.com/image/cache/catalog/demo/samsung_tab_1-500x500.jpg'
        assert ProductId49(browser_se).price_product()[8].text == '$241.99\nEx Tax: $199.99'

    # 4 тест
    def test_account(self, browser_se, url_browser_se):
        browser_se.get(f'{url_browser_se}/index.php?route=account/login')
        assert browser_se.title == 'Account Login'
        AccountLogin(browser_se) \
            .login_user(email="fdgfd@gff.com", password="5555")
        assert browser_se.title == 'My Account'
        AccountLogin(browser_se) \
            .logout() \
            .continue_click()
        assert browser_se.title == 'Your Store'
        MainPage(browser_se) \
            .my_account() \
            .menu_my_account()
        AccountLogin(browser_se) \
            .login_user(email="fdgfd@gff.com", password="5555") \
            .wish_list()
        assert browser_se.title == 'My Wish List'
        assert AccountLogin(browser_se).product_name_in_wish_list() \
               == 'My Wish List\nImage Product Name Model Stock Unit Price Action' \
                  '\nSamsung Galaxy Tab 10.1 SAM1 Pre-Order\n$199.99\nContinue'

    # 5 тест
    def test_admin(self, browser_se, url_browser_se):
        browser_se.get(f'{url_browser_se}/admin/')
        AdminPage(browser_se).button_login()
        assert browser_se.title == 'Dashboard'
        AdminPage(browser_se).button_logout()
        assert browser_se.title == 'Administration'
        AdminPage(browser_se) \
            .button_login() \
            .catalogs() \
            .products()
        assert browser_se.title == "Products"
        assert "Apple Cinema 30" in AdminPage(browser_se).table()