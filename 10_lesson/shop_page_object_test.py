import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
firefox_service = FirefoxService('C:/Users/User/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe') 
from pages.Authorization import Authorization
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.PersonalInformation import PersonalInformation

@allure.feature('Оформление заказа')
@allure.severity('critical')
@allure.title('Проверка итоговой цены при оформлении заказа')
@allure.description('Тест проверяет корректность расчёта итоговой цены после добавления товаров в корзину и заполнения контактных данных')
def test_total_price():
    driver = webdriver.Firefox(service=firefox_service)

    authorization = Authorization(driver)

    with allure.step('Открытие страницы авторизации'):
        authorization.get()
    
    with allure.step('Авторизация с учётными данными'):
        authorization.log_in()

    main_page = MainPage(driver)

    with allure.step('Добавление товаров в корзину'):
        main_page.add_items()

    with allure.step('Переход в корзину'):
        main_page.go_to_cart()

    cart_page = CartPage(driver)

    with allure.step('Переход к оформлению заказа'):
        cart_page.go_to_checkout()

    personal_info = PersonalInformation(driver)

    with allure.step('Заполнение контактных данных'):
        personal_info.contact_details()

    with allure.step('Подтверждение контактных данных и переход к итоговой цене'):
        personal_info.go_to_total_price()

    with allure.step('Получение итоговой цены'):
        total_price = personal_info.total_price()
    
    with allure.step('Проверка корректности итоговой цены'):
        assert total_price == '$58.29'

    driver.quit()