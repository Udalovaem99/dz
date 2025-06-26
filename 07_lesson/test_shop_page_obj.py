from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.FormPage import FormPage
from pages.BasketPage import BasketPage
from pages.CheckoutPage import CheckoutPage
from pages.InformationPage import InformationPage


def test_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # noqa
    form_page = FormPage(driver)
    form_page.open()
    form_page.form_authorization()

    basket_page = BasketPage(driver)
    basket_page.add_product()

    checkout_page = CheckoutPage(driver)
    checkout_page.open()
    checkout_page.checkout()

    information_page = InformationPage(driver)
    information_page.info()
    total = information_page.get_total()

    assert total == 'Total: $58.29'

    driver.quit()
