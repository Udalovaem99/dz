from selenium import webdriver
from pages.CalcPage import CalcPage


def test_calc():
    driver = webdriver.Chrome()
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.do_calc()
    calc_page.click_element()
    calc_page.expectation()
    result = calc_page.get_result()
    assert result == "15"
