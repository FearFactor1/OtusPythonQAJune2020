from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Ожидание исчезновения элемента

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.maximize_window()
driver.get("https://pagination.js.org/")
wait = WebDriverWait(driver, 10)

demo1 = driver.find_element_by_id("demo1")
items = demo1.find_elements_by_css_selector(".data-container ul li")

# Достаем 0-й элемент
print(items.pop(0).text)

pagination = demo1.find_elements_by_css_selector(".paginationjs-pages ul li")
pagination.pop(2).click()
wait.until(EC.staleness_of(items.pop(0)))
items = demo1.find_elements_by_css_selector(".data-container ul li")

print(items.pop(0).text)
driver.close()
