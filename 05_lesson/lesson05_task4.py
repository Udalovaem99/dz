from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('http://the-internet.herokuapp.com/login')

sleep(3)

log_username = '#username'
log_password = '#password'


login_page = driver.find_element(By.CSS_SELECTOR, log_username)
login_page.send_keys("tomsmith")
sleep(2)
login_page = driver.find_element(By.CSS_SELECTOR, log_password)
login_page.send_keys("SuperSecretPassword!")
sleep(2)
button = driver.find_element(By.XPATH, '//button[@type="submit"]')
button.click()

flash_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(flash_message.text)

driver.quit()
