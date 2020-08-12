

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def return_home(self):
        self.driver.find_element_by_link_text("Your Store").click()

    def return_desktop(self):
        self.driver.find_element_by_css_selector("ul.breadcrumb").find_element_by_link_text("Desktops").click()