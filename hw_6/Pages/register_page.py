from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RegisterPage:
    """
    Класс для работы со страницей регистрация и элементами на этой странице
    """
    url = "http://localhost"

    # Локаторы
    firstname_input_locator = (By.XPATH, '//div/input[@placeholder="First Name"]')
    lastname_input_locator = (By.XPATH, '//div/input[@placeholder="Last Name"]')
    link_Privacy_Policy_locator = (By.XPATH, '//div[@class="text-end"]/div/label')
    checkbox_Subscribe_locator = (By.XPATH, '//div/input[@type="checkbox"]')
    my_account_locator = (By.LINK_TEXT, "My Account")
    continue_button_locator = (By.XPATH, "//button[@type='submit']")
    register_locator = (By.LINK_TEXT, "Register")
    e_mail_locator = (By.XPATH, '//div/input[@placeholder="E-Mail"]')
    password_locator = (By.XPATH, '//div/input[@placeholder="Password"]')
    checkbox_agree_locator = (By.XPATH, '//input[@name="agree"]')
    congratulations_continue_button_locator = (By.LINK_TEXT, "Continue")
    edit_your_account_information_locator = (By.LINK_TEXT, "Edit your account information")

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    def first_name_input(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.firstname_input_locator))
        first_name = self._driver.find_element(*self.firstname_input_locator)
        first_name.clear()
        first_name.send_keys("Test_User_Firstname")

    def last_name_input(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.lastname_input_locator))
        last_name = self._driver.find_element(*self.lastname_input_locator)
        last_name.clear()
        last_name.send_keys("Test_User_Lastname")

    def email_input(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.e_mail_locator))
        email = self._driver.find_element(*self.e_mail_locator)
        email.clear()
        email.send_keys("Test_User_email_2@test.te")

    def password_input(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.password_locator))
        password = self._driver.find_element(*self.password_locator)
        password.clear()
        password.send_keys("Test_User_password")

    def agree_checkbox_click(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.checkbox_agree_locator)).click()

    def continue_button_click(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.continue_button_locator)).click()

    def congratulations_continue_button_click(self):
        WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.congratulations_continue_button_locator)).click()

    def does_edit_your_account_information_exist(self):
        edit_button = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.edit_your_account_information_locator))
        return edit_button.value_of_css_property("color")

    def move_my_account_dropdown(self):
        """
        Метод для перехода на страницу Register
        """
        my_account_link = WebDriverWait(self._driver, 2).until(
            EC.element_to_be_clickable(self.my_account_locator)
        )
        my_account_link.click()

        register_link = WebDriverWait(self._driver, 2).until(
            EC.element_to_be_clickable(self.register_locator)
        )
        register_link.click()
