from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InformationPage:
    def __init__(self, driver):
        self.driver = driver

    def info(self):
        show = WebDriverWait(self.driver, 30)
        show.until(EC.element_to_be_clickable((By.ID, "first-name"))).send_keys("Test_1") # noqa
        self.driver.find_element(By.XPATH, "//input[contains(@id, 'last-name')]").send_keys("Test_2") # noqa

        self.driver.find_element(By.XPATH, "//input[contains(@id, 'postal-code')]").send_keys("Test_3") # noqa

        self.driver.find_element(By.XPATH, "//input[contains(@id, 'continue')]").click()  # noqa

    def get_total(self):
        show = WebDriverWait(self.driver, 30)
        total = show.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
            ).text
        return total
