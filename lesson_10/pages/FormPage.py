from selenium.webdriver.common.by import By
import allure


class FormPage:
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        """
        Конструктор класса FormPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы авторизации")
    def open(self):
        """
        Открывает страницу авторизации.
        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    @allure.step("Авторизация")
    def form_authorization(self):
        """
        Вводит данные для авторизации, нажимает на кнопку для входа.
        """
        self.driver.find_element( By.XPATH, "//input[contains(@id, 'user-name')]").send_keys('standard_user')   # noqa

        self.driver.find_element(By.XPATH, "//input[contains(@id, 'password')]").send_keys('secret_sauce')  # noqa

        self.driver.find_element(By.XPATH, "//input[contains(@id, 'login-button')]").click()    # noqa
