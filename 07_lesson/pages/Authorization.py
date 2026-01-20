from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Authorization():

    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get('https://www.saucedemo.com/')

    def log_in(self):
        user_name = self._driver.find_element(By.CSS_SELECTOR, '#user-name')
        user_name.send_keys('standard_user')
        password = self._driver.find_element(By.CSS_SELECTOR, '#password')
        password.send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

