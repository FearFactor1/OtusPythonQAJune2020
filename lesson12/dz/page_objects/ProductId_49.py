from .BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductId49(BasePage):

    def wish_in_product(self):
        self.driver.find_element_by_css_selector(
            "div.col-sm-4 > div > button > i.fa.fa-heart").click()

    def alert_wish_login(self):
        alert_lg = self.driver.find_element_by_css_selector("div.alert.alert-success.alert-dismissible").text
        return alert_lg

    def compare(self):
        self.driver.find_element_by_css_selector(
            "div.col-sm-4 > div > button > i.fa.fa-exchange").click()

    def alert_success(self):
        WebDriverWait(self.driver, 3).until(
                        EC.text_to_be_present_in_element(
                            (
                                By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible"),
                            "Success: You have added Samsung Galaxy Tab 10.1 to your product comparison!\n×")
        )
        alert_sc = self.driver.find_element_by_css_selector("div.alert.alert-success.alert-dismissible").text
        return alert_sc

    def thumbnail(self):
        tml = self.driver.find_element_by_css_selector("a.thumbnail").get_attribute("href")
        return tml

    def price_product(self):
        price = self.driver.find_elements_by_css_selector("ul.list-unstyled")
        return price