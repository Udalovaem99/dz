from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def do_calc(self):
        text_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        text_input.clear()
        text_input.send_keys("45")

    def click_element(self):
        self.driver.find_element(By.XPATH, "//span[text() = '7']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '+']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '8']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '=']").click()

    def expectation(self):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))) # noqa
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")) # noqa

    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")

        return result.text
