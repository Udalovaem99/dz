from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        show = WebDriverWait(self.driver, 30)
        show.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click() # noqa

        self.driver.find_element(
        By.XPATH, "//button[contains(@id, 'add-to-cart-sauce-labs-bolt-t-shirt')]" # noqa
        ).click()

        self.driver.find_element(By.XPATH, "//button[contains(@id, 'add-to-cart-sauce-labs-onesie')]").click() # noqa

        self.driver.find_element(By.XPATH, "//a[contains(@class, 'shopping_cart_link')]").click()  # noqa