from .BasePage import BasePage


class MainPage(BasePage):

    def element_search(self):
        es = self.driver.find_element_by_css_selector(".input-lg")
        return es

    def button_search(self):
        self.driver.find_element_by_css_selector(".btn-lg").click()

    def button_dropdown(self):
        self.driver.find_element_by_css_selector(".btn-lg.dropdown-toggle").click()

    def navbar_in_home_page(self):
        navbar = self.driver.find_element_by_css_selector(".navbar-ex1-collapse").text
        return navbar

    def featured_in_home_page(self):
        featured = self.driver.find_element_by_css_selector(".transition").text
        return featured

    def bullet(self):
        self.driver.find_element_by_css_selector(".swiper-pagination-bullet-active").click()

    def img_in_main_page(self):
        img = self.driver.find_element_by_tag_name("img").get_attribute("src")
        return img

    def my_account(self):
        self.driver.find_element_by_link_text("My Account").click()
        return self

    def menu_my_account(self):
        self.driver.find_element_by_link_text("Login").click()
        return self