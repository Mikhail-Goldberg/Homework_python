from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 3)

driver.get('http://uitestingplayground.com/textinput')

my_button = driver.find_element(By.CSS_SELECTOR, 'input.form-control')
my_button.send_keys('SkyPro')
driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'button.btn.btn-primary'), 'SkyPro')
)

result = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').text
print(result)

driver.quit()