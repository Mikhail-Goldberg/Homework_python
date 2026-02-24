from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
firefox_service = FirefoxService('C:/Users/User/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe') 
from pages.Authorization import Authorization
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.PersonalInformation import PersonalInformation

def test_total_price():
    driver = webdriver.Firefox(service=firefox_service)

    authorization = Authorization(driver)
    authorization.get()
    authorization.log_in()

    main_page = MainPage(driver)
    main_page.add_items()
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    personal_info = PersonalInformation(driver)
    personal_info.contact_details()
    personal_info.go_to_total_price()
    total_price = personal_info.total_price()
    assert total_price == '$58.29'

    driver.quit()