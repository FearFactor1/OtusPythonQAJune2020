from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
driver.maximize_window()
# driver.implicitly_wait(5)

# driver.get('https://www.t-mobile.com')
# el = driver.find_element_by_xpath('//span[text()=" Search "]')
# time.sleep(10)
# el.click()
# el.send_keys('galaxy watch')

driver.get('https://beru.ru')
el = driver.find_element_by_xpath("//input[@class='mvd1wAJzjc']")
el.click()

el.send_keys('nespresso')
el.send_keys(Keys.ENTER)

# sleep(10)
el = driver.find_element_by_xpath("//div/img[@title='Кофемашина Nespresso C30 Essenza Mini черный']")

el.click()

driver.quit()
