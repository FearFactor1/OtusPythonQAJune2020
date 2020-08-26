from .BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):

    def button_login(self):
        self.driver.find_element_by_css_selector(".btn-primary").click()
        return self

    def button_logout(self):
        self.driver.find_element_by_link_text("Logout").click()

    def catalogs(self):
        self.driver.find_element_by_css_selector("li[id=menu-catalog]").click()
        return self

    def products(self):
        WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Products')]"))
        ).click()
        return self

    def table(self):
        tb = self.driver.find_element_by_css_selector(".table-hover").text
        return tb