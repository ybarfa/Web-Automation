# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# inherit TestCase Class and create a new unit_test_cases class
class PythonOrgSearch(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Test case method. It should always start with test_
    def test_search_in_python_org(self):
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("http://www.python.org")

        # assertion to confirm if title has python keyword in it
        self.assertIn("Python", driver.title)

        # locate element using name
        elem = driver.find_element(by="name", value="q")

        # send data
        elem.send_keys("pycon")

        # receive data
        elem.send_keys(Keys.RETURN)
        assert "No results found." in driver.page_source

    # cleanup method called after every unit_test_cases performed
    def tearDown(self):
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()
