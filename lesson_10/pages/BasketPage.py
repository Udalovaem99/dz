from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasketPage:
    def __init__(self, driver):
        """
        Конструктор класса BasketPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление товара")
    def add_product(self):
        """
        Добавляет товар в корзину.
        """
        show = WebDriverWait(self.driver, 30)
        show.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click() # noqa

        self.driver.find_element(
        By.XPATH, "//button[contains(@id, 'add-to-cart-sauce-labs-bolt-t-shirt')]" # noqa
        ).click()

        self.driver.find_element(By.XPATH, "//button[contains(@id, 'add-to-cart-sauce-labs-onesie')]").click() # noqa

        self.driver.find_element(By.XPATH, "//a[contains(@class, 'shopping_cart_link')]").click()  # noqa