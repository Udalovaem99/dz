from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'

    def __init__(self, driver):
        """
        Конструктор класса CalcPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(self.url)

    @allure.step("Установка таймера ожидания")
    def do_calc(self):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        """
        text_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        text_input.clear()
        text_input.send_keys("45")

    @allure.step("Нажатие кнопок калькулятора")
    def click_element(self):
        """
        Нажимает на несколько кнопок калькулятора по очереди.
        """
        self.driver.find_element(By.XPATH, "//span[text() = '7']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '+']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '8']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '=']").click()

    @allure.step("Ожидание результата") # noqa
    def expectation(self):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.
        """
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))) # noqa
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")) # noqa

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")

        return result.text
