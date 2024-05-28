from selenium import webdriver
from hw_5.Pages.register_page import RegisterPage

driver = webdriver.Chrome()
register_page = RegisterPage(driver)



def test_firstname_input():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    register_page.move_my_account_dropdown()
    assert register_page.does_firstname_input_exist() == expected_css


def test_lastname_input():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    register_page.move_my_account_dropdown()
    assert register_page.does_lastname_input_exist() == expected_css


def test_continue_button():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(255, 255, 255, 1)'
    register_page.move_my_account_dropdown()
    assert register_page.does_continue_button_exist() == expected_css


def test_link_Privacy_Policy():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(102, 102, 102, 1)'
    register_page.move_my_account_dropdown()
    assert register_page.does_link_Privacy_Policy_exist() == expected_css


def test_checkbox_Subscribe():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(0, 0, 0, 1)'
    register_page.move_my_account_dropdown()
    assert register_page.does_checkbox_Subscribe_exist() == expected_css

