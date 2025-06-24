from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    url = 'https://www.saucedemo.com/cart.html'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def checkout(self):
        show = WebDriverWait(self.driver, 30)
        show.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
            ).click()
