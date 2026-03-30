from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Authorization():
    """
    Класс для работы со страницей авторизации.
    """

    def __init__(self, driver):
        """
        Инициализация класса с веб‑драйвером.

        :param driver: экземпляр WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self._driver = driver

    def get(self) -> None:
        """
        Открывает страницу авторизации.

        :return: None
        """
        self._driver.get('https://www.saucedemo.com/')

    def log_in(self) -> None:
        """
        Выполняет вход с предустановленными учётными данными.

        :return: None
        """
        user_name = self._driver.find_element(By.CSS_SELECTOR, '#user-name')
        user_name.send_keys('standard_user')
        password = self._driver.find_element(By.CSS_SELECTOR, '#password')
        password.send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

