from selenium import webdriver
from hw_6.Pages.register_page import RegisterPage

driver = webdriver.Chrome()
register_page = RegisterPage(driver)


def test_user_register():
    expected_css = 'rgba(35, 161, 209, 1)'
    register_page.move_my_account_dropdown()
    register_page.first_name_input()
    register_page.last_name_input()
    register_page.email_input()
    register_page.password_input()
    register_page.agree_checkbox_click()
    register_page.continue_button_click()
    register_page.congratulations_continue_button_click()
    assert register_page.does_edit_your_account_information_exist() == expected_css
