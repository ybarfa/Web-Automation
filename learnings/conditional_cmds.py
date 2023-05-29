from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/login/")

username = driver.find_element(by="name", value="email")

password = driver.find_element(by="name", value="pass")

print(username.is_displayed())
print(username.is_enabled())

print(password.is_displayed())
print(password.is_enabled())

username.send_keys("barfayash2@gmail.com")
password.send_keys("$iamyash123")

driver.find_element(by="name", value="login").click()
time.sleep(10)
