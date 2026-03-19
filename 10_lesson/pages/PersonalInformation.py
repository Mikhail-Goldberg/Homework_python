from selenium.webdriver.common.by import By

class PersonalInformation:
    """
    Класс для работы со страницей ввода персональных данных.
    """

    def __init__(self, driver):
        """
        Инициализация класса с веб‑драйвером.

        :param driver: экземпляр WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self._driver = driver
    
    def contact_details(self) -> None:
        """
        Заполняет контактные данные пользователя.

        :return: None
        """
        first_name = self._driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.send_keys('Михаил')

        last_name = self._driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.send_keys('Гольдберг')

        postal_code = self._driver.find_element(By.CSS_SELECTOR, '#postal-code')
        postal_code.send_keys('191015')

    def go_to_total_price(self) -> None:
        """
        Переходит к отображению итоговой цены.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def total_price(self) -> str:
        """
        Получает итоговую цену из корзины.

        :return: текст итоговой цены
        :rtype: str
        """
        return self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text.split()[0]