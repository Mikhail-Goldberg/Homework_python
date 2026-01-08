from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://www.saucedemo.com/')

user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys('standard_user')

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')

driver.find_element(By.CSS_SELECTOR, '#login-button').click()

driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

driver.find_element(By.CSS_SELECTOR, '#checkout').click()

first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
first_name.send_keys('Михаил')

last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
last_name.send_keys('Гольдберг')

postal_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
postal_code.send_keys('191015')

driver.find_element(By.CSS_SELECTOR, '#continue').click()

total_price = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
print(total_price)

driver.quit()

assert '$58.29' in total_price