from selenium import webdriver
from Pages.register_page import RegisterPage

driver = webdriver.Chrome()
register_page = RegisterPage(driver)



def test_firstname_input():
    register_page.move_my_account_dropdown()
    assert register_page.does_firstname_input_exist()


def test_lastname_input():
    register_page.move_my_account_dropdown()
    assert register_page.does_lastname_input_exist()


def test_continue_button():
    register_page.move_my_account_dropdown()
    assert register_page.does_continue_button_exist()


def test_link_Privacy_Policy():
    register_page.move_my_account_dropdown()
    assert register_page.does_link_Privacy_Policy_exist()


def test_checkbox_Subscribe():
    register_page.move_my_account_dropdown()
    assert register_page.does_checkbox_Subscribe_exist()

# def test_move():
#     register_page.move_my_account_dropdown()


