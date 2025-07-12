from selenium import webdriver
from pages.CalcPage import CalcPage
import allure


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работу калькулятора c "
                    "указанными данными")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc():
    driver = webdriver.Chrome()
    calc_page = CalcPage(driver)
    with allure.step("Открыть калькулятор"):
        calc_page.open()
    with allure.step("Установить задержку 45 секунд"):
        calc_page.do_calc()
    with allure.step("Нажатие кнопок калькулятора по очереди"):
        calc_page.click_element()
    with allure.step("Ожидание результата"):
        calc_page.expectation()
    with allure.step("Проверка результата"):
        result = calc_page.get_result()
        assert result == "15"

    driver.quit()
