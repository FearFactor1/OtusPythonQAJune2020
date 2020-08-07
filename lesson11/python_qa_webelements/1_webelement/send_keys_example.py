import time

from conftest import DRIVERS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome(executable_path=DRIVERS + "/chromedriver")

chrome.implicitly_wait(5)
chrome.get("https://konflic.github.io/front_example/")

input_field = chrome.find_element_by_id("inp")

input_field.send_keys("Hello, my dear friend!")

time.sleep(1)

input_field.clear()

SPEED = 0.5
time.sleep(SPEED)

input_field.send_keys("-=[ ]=-")

input_field.send_keys(Keys.ARROW_LEFT)
time.sleep(SPEED)
input_field.send_keys(Keys.ARROW_LEFT)
time.sleep(SPEED)
input_field.send_keys(Keys.ARROW_LEFT)
time.sleep(SPEED)
input_field.send_keys(Keys.ARROW_LEFT)
time.sleep(SPEED)
input_field.send_keys(Keys.SPACE)
time.sleep(SPEED)
input_field.send_keys("COBRA")

for _ in range(5):
    time.sleep(SPEED)
    input_field.send_keys(Keys.BACKSPACE)

input_field.send_keys("SELENIUM")
