from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def func_wait(locator):
    def custom_func(driver):
        return True if len(driver.find_elements_by_xpath(locator)) > 0 else False
    return custom_func


driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.maximize_window()
wait = WebDriverWait(driver, 1)

driver.get('https://beru.ru')
el = driver.find_element_by_xpath("//input[@class='mvd1wAJzjc']")
el.click()

el.send_keys('часы')
el.send_keys(Keys.ENTER)

# many elements
# elements = driver.find_elements_by_xpath("//div[@class='_1Ybu1aynfr']")
elements = wait.until(lambda x: len(driver.find_elements_by_xpath("//div[@class='_1Ybu1aynfr']")) > 0)

'''
until принимает на вход callable объект, поэтому обычную функцию туда передать не получится.
Если нужно работать с какой то конкретной функцией, ее можно обернуть в func_wait, например и заложить туда логику
В данном примере удобнее воспользоваться lambd-ой
'''
# elements = wait.until(func_wait("//div[@class='_1Ybu1aynfr']"))

# print(elements)
el.click()
driver.quit()
