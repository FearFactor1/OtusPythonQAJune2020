from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.maximize_window()
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 3)

driver.get('https://beru.ru')
el = driver.find_element_by_xpath("//input[@class='mvd1wAJzjc']")
el.click()

el.send_keys('nespresso')
el.send_keys(Keys.ENTER)


el = wait.until(EC.presence_of_element_located((By.XPATH,
                                                "//div/img[@title='Кофемашина Nespresso C30 Essenza Mini черный']")))

el.click()
driver.quit()
