from conftest import DRIVERS
from selenium import webdriver

chrome = webdriver.Chrome(executable_path=DRIVERS + "/chromedriver")

chrome.implicitly_wait(5)
chrome.get("https://yandex.ru")

# search_input это объект типа WebElement
search_input = chrome.find_element_by_css_selector("input#text")

chrome.close()
