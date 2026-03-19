from selenium.webdriver.common.by import By

class CartPage:
    """
    Класс для работы со страницей корзины.
    """

    def __init__(self, driver):
        """
        Инициализация класса с веб‑драйвером.

        :param driver: экземпляр WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self._driver = driver
    
    def go_to_checkout(self) -> None:
        """
        Переходит к оформлению заказа.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()