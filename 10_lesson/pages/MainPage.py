from selenium.webdriver.common.by import By

class MainPage:
    """
    Класс для работы с главной страницей.
    """

    def __init__(self, driver):
        """
        Инициализация класса с веб‑драйвером.

        :param driver: экземпляр WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self._driver = driver

    def add_items(self) -> None:
        """
        Добавляет товары в корзину.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()