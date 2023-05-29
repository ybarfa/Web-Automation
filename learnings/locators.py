from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

sign_up = driver.find_element(By.LINK_TEXT, "Register")
sign_up.click()
time.sleep(2)

check_box = driver.find_element(By.XPATH, '//input[@id="gender-male"]')
check_box.click()

first_name = driver.find_element(By.XPATH, '//input[@name="FirstName"]')
first_name.send_keys("Aman")

last_name = driver.find_element(By.XPATH, '//input[@id="LastName"]')
last_name.send_keys("Barfa")

DOB_day = driver.find_element(By.XPATH, '//select[@name="DateOfBirthDay"]')
DOB_day.click()
select_day = Select(DOB_day)
select_day.select_by_value("6")

DOB_month = driver.find_element(By.XPATH, '//select[@name="DateOfBirthMonth"]')
DOB_month.click()
select_month = Select(DOB_month)
select_month.select_by_value("10")

DOB_year = driver.find_element(By.XPATH, '//select[@name="DateOfBirthYear"]')
DOB_year.click()
select_year = Select(DOB_year)
select_year.select_by_value("2001")

email = driver.find_element(By.XPATH, '//input[@id="Email"]')
email.send_keys("amanbarfa203@gmail.com")

password = driver.find_element(By.XPATH, '//input[@id="Password"]')
password.send_keys("$amaman123")

confirm_pass = driver.find_element(By.XPATH, '//input[@id="ConfirmPassword"]')
confirm_pass.send_keys("$amaman123")

register = driver.find_element(By.XPATH, '//button[@id="register-button"]')
register.click()
time.sleep(5)
