from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # noqa

driver.get('http://uitestingplayground.com/dynamicid')
sleep(2)

blue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Button')]") # noqa
blue_button.click()

sleep(2)
