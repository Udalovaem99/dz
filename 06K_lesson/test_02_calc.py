from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # noqa


def main(driver):
    driver.maximize_window()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html') # noqa

    text_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    text_input.clear()
    text_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))) # noqa

    WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")) # noqa


def test_calc():
    driver = webdriver.Chrome()
    main(driver)
    res = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert res == "15"


driver.quit()
