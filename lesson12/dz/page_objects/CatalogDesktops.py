from .BasePage import BasePage


class CatalogDesktops(BasePage):

    def img_thumbnail(self):
        img = self.driver.find_element_by_css_selector("img.img-thumbnail").get_attribute("src")
        return img

    def refine_search_pc(self):
        self.driver.find_element_by_link_text("PC (0)").click()

    def refine_search_mac(self):
        self.driver.find_element_by_link_text("Mac (1)").click()

    def desktop_colomn(self):
        colomns = self.driver.find_element_by_css_selector("div.list-group").text
        return colomns