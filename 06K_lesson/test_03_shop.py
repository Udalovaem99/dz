from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) # noqa


def main(driver):
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.XPATH, "//input[contains(@id, 'user-name')]"
        ).send_keys('standard_user')

    driver.find_element(
        By.XPATH, "//input[contains(@id, 'password')]"
        ).send_keys('secret_sauce')

    driver.find_element(
        By.XPATH, "//input[contains(@id, 'login-button')]"
        ).click()

    show = WebDriverWait(driver, 30)
    show.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()

    driver.find_element(
        By.XPATH, "//button[contains(@id, 'add-to-cart-sauce-labs-bolt-t-shirt')]" # noqa
        ).click()

    driver.find_element(
        By.XPATH, "//button[contains(@id, 'add-to-cart-sauce-labs-onesie')]"
        ).click()

    driver.find_element(
        By.XPATH, "//a[contains(@class, 'shopping_cart_link')]"
        ).click()

    show.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    show.until(
        EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys("Test_1")

    driver.find_element(
        By.XPATH, "//input[contains(@id, 'last-name')]"
        ).send_keys("Test_2")

    driver.find_element(
        By.XPATH, "//input[contains(@id, 'postal-code')]"
        ).send_keys("Test_3")

    driver.find_element(
        By.XPATH, "//input[contains(@id, 'continue')]"
        ).click()

    total = show.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")) # noqa
        ).text

    return total


def test_buy():
    driver = webdriver.Firefox()
    total = main(driver)
    driver.quit()
    assert total == 'Total: $58.29'


driver.quit()
