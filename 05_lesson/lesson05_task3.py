from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) # noqa

driver.get('http://the-internet.herokuapp.com/inputs')
number = driver.find_element(By.XPATH, '//input[@type="number"]')
number.send_keys("Sky", Keys.RETURN)
sleep(2)
number.clear()
number = driver.find_element(By.XPATH, '//input[@type="number"]')
number.send_keys("Pro", Keys.RETURN)
sleep(2)


driver.quit()
