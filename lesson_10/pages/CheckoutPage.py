from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    url = 'https://www.saucedemo.com/cart.html'

    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы коризины")
    def open(self):
        """
        Открывает страницу корзины.
        """
        self.driver.get(self.url)

    @allure.step("Нажатие кнопки оформления заказа")
    def checkout(self):
        """
        Открывает страницу оформления заказа.
        """
        show = WebDriverWait(self.driver, 30)
        show.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
            ).click()
