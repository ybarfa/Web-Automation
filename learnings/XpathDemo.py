from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

search_box = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_box.send_keys("Tshirts for men")

search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
search_button.click()

driver_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-medium a-text-italic']")))
