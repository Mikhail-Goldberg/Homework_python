from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
edge_service = EdgeService('C:/Users/User/Downloads/edgedriver_win64/msedgedriver.exe')
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=edge_service)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
first_name.send_keys('Иван')

last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
last_name.send_keys('Петров')

address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
address.send_keys('Ленина, 55-3')

city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
city.send_keys('Москва')

country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
country.send_keys('Россия')

email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
email.send_keys('test@skypro.com')

phone_number = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
phone_number.send_keys('+7985899998787')

job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
job_position.send_keys('QA')

company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
company.send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click()

element = driver.find_element(By.CSS_SELECTOR, '#zip-code')
background_color = element.value_of_css_property("background-color")
assert background_color == 'rgba(248, 215, 218, 1)'

valid_elements = [
    'first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company'
]

for elements in valid_elements:
    classes = driver.find_element(By.ID, elements).get_attribute('class')
    assert 'alert-success' in classes

driver.quit()