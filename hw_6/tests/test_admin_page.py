from selenium import webdriver
from hw_6.Pages.admin import AdminPage

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
    admin_page.add_new_click()
    admin_page.make_new_product()
    admin_page.back_button_click()
    admin_page.sort_by_quantity()
    assert admin_page.check_product_in_table() == True
    admin_page.logout_button_lockator

def test_item_delete():
    """
        Тест проверяет возможность удаления товара
        """
    admin_page.username_input()
    admin_page.password_input()
    admin_page.login_button_click()
    admin_page.move_to_addNew_product()
    admin_page.sort_by_quantity()
    admin_page.checkbox_click()
    admin_page.delete_button_click()
    admin_page.alert_click()
    admin_page.logout_button_lockator
    assert admin_page.check_product_in_table() == False
    admin_page.logout_button_lockator


