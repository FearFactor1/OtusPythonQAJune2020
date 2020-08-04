from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.maximize_window()
wait = WebDriverWait(driver, 5)


driver.get('https://beru.ru')
el = driver.find_element_by_xpath("//input[@class='mvd1wAJzjc']")
el.click()

el.send_keys('nespresso')
el.send_keys(Keys.ENTER)

# wait.until(EC.title_contains('nespresso'))
el = wait.until(EC.presence_of_element_located((By.XPATH,
                                           "//div/img[@title='Кофемашина Nespresso C30 Essenza Mini черный']")))

# el = wait.until(EC.text_to_be_present_in_element((By.XPATH,
#                                                   "//div/img[@title='Кофемашина Nespresso C30 Essenza Mini черный']"),
#                                                  text_='Кофемашина Nespresso C30 Essenza Mini черный'))

driver.quit()
