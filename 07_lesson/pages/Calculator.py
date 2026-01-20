from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator():

    def __init__(self, driver):
        self._driver = driver

    def delay(self):
        self.wait = WebDriverWait(self._driver, 45)
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        element = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        element.clear()
        element.send_keys('45')
    
    def numbers(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def result(self):
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="screen"]'), '15')
        )

        return self._driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text