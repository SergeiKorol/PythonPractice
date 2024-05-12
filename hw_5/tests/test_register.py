from selenium import webdriver
from Pages.register_page import RegisterPage

driver = webdriver.Chrome()
register_page = RegisterPage(driver)


def test_firstname_input():
    assert register_page.does_firstname_input_exist()


def test_lastname_input():
    assert register_page.does_lastname_input_exist()


def test_continue_button():
    assert register_page.does_continue_button_exist()


def test_link_Privacy_Policy():
    assert register_page.does_link_Privacy_Policy_exist()


def test_checkbox_Subscribe():
    assert register_page.does_checkbox_Subscribe_exist()
