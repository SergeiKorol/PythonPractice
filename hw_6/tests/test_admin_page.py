from selenium import webdriver
from hw_6.Pages.admin import AdminPage

driver = webdriver.Chrome()
admin_page = AdminPage(driver)


def test_add_item():
    admin_page.username_input()
    admin_page.password_input()
    admin_page.login_button_click()
    admin_page.catalog_click()
    admin_page.products_click()


