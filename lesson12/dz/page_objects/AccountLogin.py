from .BasePage import BasePage


class AccountLogin(BasePage):

    def input_email(self):
        email = self.driver.find_element_by_css_selector("input[id=input-email]")
        return email

    def input_password(self):
        password = self.driver.find_element_by_css_selector("input[id=input-password]")
        return password

    def button_login(self):
        self.driver.find_element_by_css_selector("input[value=Login]").click()

    def logout(self):
        self.driver.find_element_by_link_text("Logout").click()

    def continue_click(self):
        self.driver.find_element_by_link_text("Continue").click()

    def wish_list(self):
        self.driver.find_element_by_link_text("Wish List").click()

    def product_name_in_wish_list(self):
        product = self.driver.find_element_by_css_selector("div[id=content]").text
        return product