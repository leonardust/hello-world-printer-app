from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

class SimpleTest(unittest.TestCase):
   def setUp(self):
       self.driver = webdriver.Chrome(executable_path='/home/tester/Pobrane/chromedriver')
       self.driver.maximize_window()
       self.driver.get('http://localhost:5000')

   def test_content_page(self):
       # locators
       find_content = "//body[contains(text(), 'Lukasz Hello World)]"
       # steps
       WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, find_content)))

   def tearDown(self):
       self.driver.quit()

if __name__ == '__main__':
    unittest.main()
