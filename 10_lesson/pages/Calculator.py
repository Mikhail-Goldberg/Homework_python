from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator():
    """
    Класс для работы с калькулятором на тестовой странице.
    """

    def __init__(self, driver):
        """
        Инициализация класса с веб‑драйвером.

        :param driver: экземпляр WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self._driver = driver

    def delay(self) -> None:
        """
        Настраивает задержку калькулятора и открывает страницу.

        :return: None
        """
        self.wait = WebDriverWait(self._driver, 45)
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        element = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        element.clear()
        element.send_keys('45')
    
    def numbers(self) -> None:
        """
        Вводит последовательность чисел и операций: 7 + 8 =.

        :return: None
        """
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def result(self) -> str:
        """
        Ожидает и возвращает результат вычисления.

        :return: текст результата
        :rtype: str
        """
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="screen"]'), '15')
        )

        return self._driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text