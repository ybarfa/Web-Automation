# EXPLICIT WAIT PRACTICE SITE
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("http://the-internet.herokuapp.com/dynamic_loading/1")
#
# start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
# time.sleep(2)
# start_button.click()
#
# wait = WebDriverWait(driver, 10)
# message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
#
# print(message.text)
#
# driver.quit()


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.wingslifestyle.in/")

search = driver.find_element(By.XPATH, '//a[@class="page-open-popup-search hint--bounce hint--bottom header-icon icon-set-01 icon-display--icon"]')
search.click()
time.sleep(3)
textbox = driver.find_element(By.CLASS_NAME, "search-field")
textbox.send_keys("Wings Phantom 260")

search_button = driver.find_element(By.XPATH, '//span[@class="search-btn-icon"]')
search_button.click()

wait = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//div[@class="product-hover-image"]')))
search_result = driver.find_element(By.XPATH, '//div[@class="product-hover-image"]')
search_result.click()

time.sleep(10)

