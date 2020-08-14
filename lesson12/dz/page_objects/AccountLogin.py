from .BasePage import BasePage


class AccountLogin(BasePage):

    LOGIN_EMAIL_INPUT = {'css': '#input-email'}
    LOGIN_PASSWORD_INPUT = {'css': '#input-password'}
    LOGIN_BUTTON = {'css': 'input[value=Login]'}

    def login_user(self, email, password):
        self._input(self.LOGIN_EMAIL_INPUT, email)
        self._input(self.LOGIN_PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)
        return self

    def logout(self):
        self.driver.find_element_by_link_text("Logout").click()
        return self

    def continue_click(self):
        self.driver.find_element_by_link_text("Continue").click()
        return self

    def wish_list(self):
        self.driver.find_element_by_link_text("Wish List").click()
        return self

    def product_name_in_wish_list(self):
        product = self.driver.find_element_by_css_selector("div[id=content]").text
        return product