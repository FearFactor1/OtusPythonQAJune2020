from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test:

    def test_go_to_card(self, driver, wait):
        driver.get('https://beru.ru')

        # Переход на страницу каталог товаров
        el = driver.find_element_by_css_selector("[data-zone-name='headerCatalog']")
        el.click()

        el = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Бытовая техника")))
        # driver.find_element_by_partial_link_text('Бытовая техника')
        el.click()

        title_page = driver.find_element_by_xpath("//h1[@class='rPzd7GVCYx _1s00-3EuYB']")
        assert title_page.text == 'Бытовая техника'
