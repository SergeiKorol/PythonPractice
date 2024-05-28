from selenium import webdriver
from hw_5.Pages.admin import AdminPage

driver = webdriver.Chrome()
admin_page = AdminPage(driver)


def test_username_input():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    assert admin_page.does_username_input_exist() == expected_css


def test_password_input():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    assert admin_page.does_password_input_exist() == expected_css


def test_login_button():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(255, 255, 255, 1)'
    assert admin_page.does_login_button_exist() == expected_css


def test_promo_link():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(30, 145, 207, 1)'
    assert admin_page.does_promo_link_exist() == expected_css


def test_data_input_form():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    assert admin_page.does_data_input_form_exist() == expected_css
