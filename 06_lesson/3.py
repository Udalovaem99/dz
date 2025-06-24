from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # noqa
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # noqa
browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html") # noqa
waiter = WebDriverWait(browser, 30)

imgs = waiter.until(EC.presence_of_all_elements_located((By.ID, 'landscape')))

wait = WebDriverWait(browser, 10)
award_element = wait.until(EC.presence_of_element_located((By.ID, "award")))
src = award_element.get_attribute("src")
print(src)
browser.quit()
