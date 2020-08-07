from conftest import DRIVERS
from selenium import webdriver

firefox = webdriver.Firefox(executable_path=DRIVERS + "/geckodriver")
firefox.implicitly_wait(5)
firefox.get("https://yandex.ru")

home_tabs = firefox.find_element_by_css_selector(".home-tabs3")

html = home_tabs.get_property("innerHTML")
print(html)

attr = home_tabs.get_attribute("data-bem")
print(attr)

css = home_tabs.value_of_css_property("margin-bottom")
print(css)

firefox.close()
