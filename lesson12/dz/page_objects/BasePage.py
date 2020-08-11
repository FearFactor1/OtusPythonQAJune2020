


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def retun_home(self):
        self.driver.find_element_by_link_text("Your Store").click()