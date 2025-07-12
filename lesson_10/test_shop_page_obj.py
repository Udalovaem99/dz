from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.FormPage import FormPage
from pages.BasketPage import BasketPage
from pages.CheckoutPage import CheckoutPage
from pages.InformationPage import InformationPage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@allure.title("Тестирование интернет-магазина")
@allure.description("Тест на проверку функциональности интернет-магазина")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # noqa
    form_page = FormPage(driver)
    with allure.step("Открыть сайт"):
        form_page.open()
    with allure.step("Заполнить форму авторизации"):
        form_page.form_authorization()

    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.dismiss()
    except TimeoutException:
        pass

    basket_page = BasketPage(driver)
    with allure.step("Добавить товар в корзину"):
        basket_page.add_product()

    checkout_page = CheckoutPage(driver)
    with allure.step("Открыть страницу оформления заказа"):
        checkout_page.open()
    with allure.step("Нажатие кнопки оформления заказа"):
        checkout_page.checkout()

    information_page = InformationPage(driver)
    with allure.step("Ввести данные для оформления заказа"):
        information_page.info()
    with allure.step("Проверка результата"):
        total = information_page.get_total()
        assert total == 'Total: $58.29'

    driver.quit()
