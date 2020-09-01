from lesson14.dz.page_objects.MainPage import MainPage
from lesson14.dz.page_objects.BasePage import BasePage
from lesson14.dz.page_objects.CatalogDesktops import CatalogDesktops
from lesson14.dz.page_objects.ProductId_49 import ProductId49
from lesson14.dz.page_objects.AccountLogin import AccountLogin
from lesson14.dz.page_objects.AdminPage import AdminPage
import allure


class TestClassOpencart:

    # 1 тест
    @allure.link('https://demo.opencart.com/')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('story')
    @allure.feature('epic')
    @allure.title('main_page')
    def test_main_page(self, browser_se, url_browser_se):
        browser_se.get(url_browser_se)
        assert browser_se.title == 'Your Store'
        with allure.step("На главной странице ищу продукт: Apple Cinema 30"):
            element_search = MainPage(browser_se).element_search()
            element_search.send_keys("Apple Cinema 30")
            MainPage(browser_se).button_search()
            assert browser_se.current_url == \
                'https://demo.opencart.com/index.php?route=product/search&search=Apple%20Cinema%2030'
            assert browser_se.title == 'Search - Apple Cinema 30'
        with allure.step("Возвращаюсь обратно на главную страницу"):
            BasePage(browser_se).return_home()
            assert browser_se.title == 'Your Store'
        with allure.step("Проверяю, что на главной странице есть меню с выбором категорий"):
            MainPage(browser_se).button_dropdown()
            assert MainPage(browser_se).navbar_in_home_page() == \
                'Desktops\nLaptops & Notebooks\nComponents\nTablets\nSoftware\nPhones & PDAs\nCameras\nMP3 Players'
        with allure.step("Проверяею, что есть MacBook в меню категорий"):
            assert 'MacBook' in MainPage(browser_se).featured_in_home_page()
        with allure.step("Смотрю, что в рекламном отсеке есть нужная фотка"):
            MainPage(browser_se).bullet()
            assert MainPage(browser_se).img_in_main_page() == \
                'https://demo.opencart.com/image/cache/catalog/demo/banners/MacBookAir-1140x380.jpg'

    # 2 тест
    @allure.link('https://demo.opencart.com/index.php?route=product/category&path=20')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('catalog_desktops')
    def test_catalog_desktops(self, browser_se, url_browser_se):
        browser_se.get(f'{url_browser_se}/index.php?route=product/category&path=20')
        with allure.step("Смотрю, что открыто меню Desktops и есть картинка"):
            assert browser_se.title == 'Desktops'
            assert CatalogDesktops(browser_se).img_thumbnail() == \
                'https://demo.opencart.com/image/cache/catalog/demo/compaq_presario-80x80.jpg'
        with allure.step("Смотрю, что каталог ПК кликабельный"):
            CatalogDesktops(browser_se).refine_search_pc()
            assert browser_se.current_url == 'https://demo.opencart.com/index.php?route=product/category&path=20_26'
        with allure.step("возвращаюсь в меню Desktop"):
            BasePage(browser_se).return_desktop()
            assert browser_se.title == 'Desktops'
        with allure.step("Смотрю, что каталог МАК кликабельный"):
            CatalogDesktops(browser_se).refine_search_mac()
            assert browser_se.current_url == 'https://demo.opencart.com/index.php?route=product/category&path=20_27'
        with allure.step("возвращаюсь в меню Desktop"):
            BasePage(browser_se).return_desktop()
            assert browser_se.title == 'Desktops'
        assert "Laptops & Notebooks (5)" in CatalogDesktops(browser_se).desktop_colomn()

    # 3 тест
    @allure.link('https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('product_id_49')
    def test_product_id_49(self, browser_se, url_browser_se):
        with allure.step("Проверяем , что товар под айди 49 Самсунг"):
            browser_se.get(f'{url_browser_se}/index.php?route=product/product&path=57&product_id=49')
            assert browser_se.title == 'Samsung Galaxy Tab 10.1'
        with allure.step("Добавляем Самсунг в список любимых продуктов"):
            ProductId49(browser_se).wish_in_product()
            assert ProductId49(browser_se).alert_wish_login() == \
                'You must login or create an account to save Samsung Galaxy Tab 10.1 to your wish list!\n×'
        with allure.step("добавляем Самсунг в список сравнения"):
            ProductId49(browser_se).compare()
            assert ProductId49(browser_se).alert_success() == \
                'Success: You have added Samsung Galaxy Tab 10.1 to your product comparison!\n×'
        with allure.step("Проверяем наличие фотки и стоимости"):
            assert ProductId49(browser_se).thumbnail() == \
                'https://demo.opencart.com/image/cache/catalog/demo/samsung_tab_1-500x500.jpg'
            assert ProductId49(browser_se).price_product()[8].text == '$241.99\nEx Tax: $199.99'

    # 4 тест
    @allure.link('https://demo.opencart.com/index.php?route=account/login')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title('account')
    def test_account(self, browser_se, url_browser_se):
        browser_se.get(f'{url_browser_se}/index.php?route=account/login')
        with allure.step("Вводим логин и пароль"):
            assert browser_se.title == 'Account Login'
            AccountLogin(browser_se) \
                .login_user(email="fdgfd@gff.com", password="5555")
            assert browser_se.title == 'My Account'
        with allure.step("делаем раздлгин"):
            AccountLogin(browser_se) \
                .logout() \
                .continue_click()
            assert browser_se.title == 'Your Store'
        with allure.step("Делаем логин"):
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
    @allure.link('https://demo.opencart.com/admin/')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('admin')
    def test_admin(self, browser_se, url_browser_se):
        browser_se.get(f'{url_browser_se}/admin/')
        with allure.step("Делаем логин"):
            AdminPage(browser_se).button_login()
            assert browser_se.title == 'Dashboard'
        with allure.step("Делаем разлогин"):
            AdminPage(browser_se).button_logout()
            assert browser_se.title == 'Administration'
        with allure.step("Переходим в таблицу и ищём Applq"):
            AdminPage(browser_se) \
                .button_login() \
                .catalogs() \
                .products()
            assert browser_se.title == "Products"
            assert "Apple Cinema 30" in AdminPage(browser_se).table()