from selenium import webdriver
from hw_6.Pages.main import MainPage

driver = webdriver.Chrome()
main_page = MainPage(driver)


def test_choose_currency():
    main_page.get_current_currency()
    main_page.currency_click()
    main_page.choose_another_currency()
    main_page.get_current_currency()
