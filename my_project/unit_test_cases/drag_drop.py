# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException
# from my_project.utils.xpath import *
# import json
# import os
#
# current_directory = os.getcwd()
# parent_directory = os.path.dirname(current_directory)
# config_path = os.path.join(parent_directory, "configuration", "config.json")
#
# with open(config_path, "r") as configuration:
#     config_data = json.load(configuration)
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(config_data["url"])
#     driver.maximize_window()
#
#     drag_drop = driver.find_element(By.XPATH, herokuapp_feilds["Drag_Drop"])
#     drag_drop.click()
#
#     a = driver.find_element(By.XPATH, '//div[@id="column-a"]')
#     b = driver.find_element(By.XPATH, '//div[@id="column-b"]')
#
#     action_chains = ActionChains(driver)
#     action_chains.drag_and_drop(a, b).perform()
#
#     result_text = b.text
#     expected_text = "A"
#     if result_text == expected_text:
#         assert True, "Drag and drop successful!"
#     else:
#         assert False, "Drag and drop failed."
#
# except NoSuchElementException:
#     print("No Such Element Found.")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set the path to the chromedriver executable
webdriver_service = Service('path_to_chromedriver')
# Instantiate the WebDriver
driver = webdriver.Chrome(service=webdriver_service)
# Navigate to the webpage with the drag and drop elements
driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# Execute JavaScript to simulate drag and drop
driver.execute_script("""
    (function() {
        var source = arguments[0];
        var target = arguments[1];
        // Load jquery.simulate.js library
        var jquerySimulateScript = document.createElement('script');
        jquerySimulateScript.src = 'https://rawgithub.com/jquery/jquery-simulate/master/jquery.simulate.js';
        document.head.appendChild(jquerySimulateScript);
        // Simulate drag and drop action
        jQuery(source).simulate('drag-n-drop', { dragTarget: target });
    })(arguments[0], arguments[1]);
""", driver.find_element(By.ID, 'column-a'), driver.find_element(By.ID, 'column-b'))
# Close the browser
driver.quit()
