from selenium.webdriver.common.by import By


class FormPage:
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def form_authorization(self):
        self.driver.find_element( By.XPATH, "//input[contains(@id, 'user-name')]").send_keys('standard_user')   # noqa

        self.driver.find_element(By.XPATH, "//input[contains(@id, 'password')]").send_keys('secret_sauce')  # noqa

        self.driver.find_element(By.XPATH, "//input[contains(@id, 'login-button')]").click()    # noqa
