import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_service = ChromeService('C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
from pages.Calculator import Calculator

@allure.feature('Калькулятор')
@allure.severity('critical')
@allure.title('Проверка результата сложения 7 + 8')
@allure.description('Тест проверяет, что калькулятор правильно вычисляет сумму 7 + 8 и возвращает 15')
def test_get_number():
    """
    Тест для проверки корректности работы калькулятора:
    1. Открывает страницу калькулятора.
    2. Устанавливает задержку 45 секунд.
    3. Вводит последовательность: 7 + 8 =.
    4. Ожидает результата.
    5. Проверяет, что результат равен 15.
    """
    driver = webdriver.Chrome(service=chrome_service)
    
    calculator = Calculator(driver)

    with allure.step('Открытие страницы калькулятора и настройка задержки'):
        calculator.delay()
    
    with allure.step('Ввод чисел и операции: 7 + 8 ='):
        calculator.numbers()
    
    with allure.step('Ожидание и получение результата'):
        result = calculator.result()
    
    with allure.step('Проверка результата вычисления'):
        assert result == '15'

    driver.quit()