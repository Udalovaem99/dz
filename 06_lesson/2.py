from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # noqa

browser.get("http://uitestingplayground.com/textinput")

element = browser.find_element(By.CSS_SELECTOR, "#newButtonName")
element.clear()
element.send_keys("SkyPro")

browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()

print(browser.find_element(By.CSS_SELECTOR, "#updatingButton").text)

browser.quit()
