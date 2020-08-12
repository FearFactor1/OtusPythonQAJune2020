from .BasePage import BasePage


class MainPage(BasePage):

   def element_search(self):
       es = self.driver.find_element_by_css_selector("input.form-control.input-lg")
       return es

   def button_search(self):
       self.driver.find_element_by_css_selector("button.btn.btn-default.btn-lg").click()

   def button_dropdown(self):
       self.driver.find_element_by_css_selector(
           "button.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle").click()

   def navbar_in_home_page(self):
       navbar = self.driver.find_element_by_css_selector(
           "div.collapse.navbar-collapse.navbar-ex1-collapse").text
       return navbar

   def featured_in_home_page(self):
       featured = self.driver.find_element_by_css_selector("div.product-thumb.transition").text
       return featured

   def bullet(self):
       self.driver.find_element_by_css_selector(
           "span.swiper-pagination-bullet.swiper-pagination-bullet-active").click()

   def img_in_main_page(self):
       img = self.driver.find_element_by_tag_name("img").get_attribute("src")
       return img

   def my_account(self):
       self.driver.find_element_by_link_text("My Account").click()

   def menu_my_account(self):
       self.driver.find_element_by_link_text("Login").click()