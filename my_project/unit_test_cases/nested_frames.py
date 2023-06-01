from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

element=driver.find_element(By.XPATH,'//a[@href="/nested_frames"]')
element.click()

frame_top = driver.find_element(By.XPATH, '//frame[@name="frame-top"]')
driver.switch_to.frame(frame_top)

frame_left = driver.find_element(By.XPATH, '//frame[@name="frame-left"]')
driver.switch_to.frame(frame_left)
text4 = driver.find_element(By.XPATH, '//body[contains(text(), "LEFT")]').text
print(text4)

driver.switch_to.parent_frame()
frame_middle = driver.find_element(By.XPATH, '//frame[@name="frame-middle"]')
driver.switch_to.frame(frame_middle)
text=driver.find_element(By.XPATH,'//div[@id="content"]').text
print(text)

driver.switch_to.parent_frame()
frame_right = driver.find_element(By.XPATH, '//frame[@name="frame-right"]')
driver.switch_to.frame(frame_right)
text2 = driver.find_element(By.XPATH, '//body[contains(text(), "RIGHT")]').text
print(text2)

driver.switch_to.default_content()
frame_bottom = driver.find_element(By.XPATH, '//frame[@name="frame-bottom"]')
driver.switch_to.frame(frame_bottom)
text3=driver.find_element(By.XPATH, '//body[contains(text(), "BOTTOM")]').text
print(text3)
time.sleep(3)
