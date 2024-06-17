from selenium import webdriver
from hw_5.Pages.main import MainPage

driver = webdriver.Chrome()
main_page = MainPage(driver)


def test_search_field():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    assert main_page.does_search_field_exist() == expected_css


def test_desktop_dropdown():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(35, 161, 209, 1)'
    assert main_page.does_opencart_exist() == expected_css


def test_button_total():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(68, 68, 68, 1)'
    assert main_page.does_featured_exist() == expected_css


def test_footer():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(226, 226, 226, 1)'
    assert main_page.does_footer_exist() == expected_css


def test_wishlist():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(136, 136, 136, 1)'
    assert main_page.does_wishlist_exist() == expected_css


def test_currency_dropdown():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(204, 204, 204, 1)'
    assert main_page.does_opencart_link_exist() == expected_css
