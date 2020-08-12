from .BasePage import BasePage


class AdminPage(BasePage):

    def button_login(self):
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()

    def button_logout(self):
        self.driver.find_element_by_link_text("Logout").click()

    def catalogs(self):
        self.driver.find_element_by_css_selector("li[id=menu-catalog]").click()

    def products(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()

    def table(self):
        tb = self.driver.find_element_by_css_selector("table.table.table-bordered.table-hover").text
        return tb