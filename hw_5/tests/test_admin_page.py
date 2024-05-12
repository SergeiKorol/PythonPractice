from selenium import webdriver
from Pages.admin import AdminPage

driver = webdriver.Chrome()
admin_page = AdminPage(driver)


def test_username_input():
    assert admin_page.does_username_input_exist()


def test_password_input():
    assert admin_page.does_password_input_exist()


def test_login_button():
    assert admin_page.does_login_button_exist()


def test_promo_link():
    assert admin_page.does_promo_link_exist()


def test_data_input_form():
    assert admin_page.does_data_input_form_exist()
