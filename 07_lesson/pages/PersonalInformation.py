from selenium.webdriver.common.by import By

class PersonalInformation:

    def __init__(self, driver):
        self._driver = driver
    
    def contact_details(self):
        first_name = self._driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.send_keys('Михаил')

        last_name = self._driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.send_keys('Гольдберг')

        postal_code = self._driver.find_element(By.CSS_SELECTOR, '#postal-code')
        postal_code.send_keys('191015')

    def go_to_total_price(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def total_price(self):
        return self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text.split()[0]