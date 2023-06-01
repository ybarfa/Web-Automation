# def adder():
#     a = 2
#     b = 3
#     if a == b:
#         assert True, "a is equal to b"
#     else:
#         assert False, "a is not equal to b"
# adder()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.instagram.com/")
#
# username = driver.find_element(By.XPATH, '//input[@aria-label="Phone number, username, or email"]')
# username.send_keys("barfayash2@gmail.com")


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/")
# driver.maximize_window()
#
# element=driver.find_element(By.XPATH,'//a[@href="/nested_frames"]')
# element.click()
#
# frame_top = driver.find_element(By.XPATH, '//frame[@name="frame-top"]')
# driver.switch_to.frame(frame_top)
#
# frame_left = driver.find_element(By.XPATH, '//frame[@name="frame-left"]')
# driver.switch_to.frame(frame_left)
#
#
# driver.switch_to.parent_frame()
# frame_middle = driver.find_element(By.XPATH, '//frame[@name="frame-middle"]')
# driver.switch_to.frame(frame_middle)
#
# driver.switch_to.parent_frame()
# frame_right = driver.find_element(By.XPATH, '//frame[@name="frame-right"]')
# driver.switch_to.frame(frame_right)
#
# driver.switch_to.parent_frame()
# frame_bottom = driver.find_element(By.XPATH, '//frame[@name="frame-bottom"]')
# driver.switch_to.frame(frame_bottom)
#
# time.sleep(3)
