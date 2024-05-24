from selenium import webdriver
from hw_6.Pages.admin import AdminPage
import time

driver = webdriver.Chrome()
admin_page = AdminPage(driver)

#добавить проверку существует ли товар
def test_item_add():
    """
    Тест проверяет возможность добавления товара
    """
    admin_page.username_input()
    admin_page.password_input()
    admin_page.login_button_click()
    admin_page.move_to_addNew_product()
    admin_page.make_new_product()
    admin_page.back_button_click()
    admin_page.sort_by_quantity()
    assert admin_page.check_product_in_table()

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
