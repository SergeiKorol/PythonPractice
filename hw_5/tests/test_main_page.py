from selenium import webdriver
from Pages.main import MainPage

driver = webdriver.Chrome()
main_page = MainPage(driver)


def test_search_field():
    assert main_page.does_search_field_exist()


def test_category_dropdown():
    assert main_page.does_category_dropdown_exist()


def test_button_total():
    assert main_page.does_button_total_exist()


def test_footer():
    assert main_page.does_footer_exist()


def test_wishlist():
    assert main_page.does_wishlist_exist()


def test_currency_dropdown():
    assert main_page.does_currency_dropdown_exist()
