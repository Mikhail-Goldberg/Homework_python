from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_service = ChromeService('C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
from pages.Calculator import Calculator

def test_get_number():
    driver = webdriver.Chrome(service=chrome_service)
    
    calculator = Calculator(driver)
    calculator.delay()
    calculator.numbers()
    result = calculator.result()
    assert result == '15'

    driver.quit()