import requests

# Specify the username and password
username = "admin"
password = "admin"

url = f"https://{username}:{password}@the-internet.herokuapp.com/download_secure"

response = requests.get(url)

if response.status_code == 200:
    print("Authentication successful!")
else:
    print("Authentication failed!")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com")
driver.maximize_window()

download = driver.find_element(By.XPATH, '//a[@href="download_secure/uploadImage.png"]')
download.click()
