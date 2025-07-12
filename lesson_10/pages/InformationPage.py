from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InformationPage:
    def __init__(self, driver):
        """
        Конструктор класса InformationPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Ввод данных для оформления заказа")
    def info(self):
        """
        Вводит данные для оформления заказа, нажимает на кнопку продолжить.
        """
        show = WebDriverWait(self.driver, 60)
        show.until(EC.element_to_be_clickable((By.ID, "first-name"))).send_keys("Test_1") # noqa
        self.driver.find_element(By.XPATH, "//input[contains(@id, 'last-name')]").send_keys("Test_2") # noqa

        self.driver.find_element(By.XPATH, "//input[contains(@id, 'postal-code')]").send_keys("Test_3") # noqa

        self.driver.find_element(By.XPATH, "//input[contains(@id, 'continue')]").click()  # noqa

    @allure.step("Вывод итоговой стоимости товара с экрана корзины")
    def get_total(self):
        """
        Выводит итоговую стоимость товара с экрана корзины.
        :return: str — текст результата на экране корзины.
        """
        show = WebDriverWait(self.driver, 30)
        total = show.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
            ).text
        return total
