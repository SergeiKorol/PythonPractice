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
    my_account_locator = (By.XPATH, "//a[contains(@href,'route=account/account')]")
    continue_button_locator = (By.XPATH, "//button[@type='submit']")
    register_locator = (By.XPATH, '//a[@class="dropdown-toggle show" and @data-bs-toggle="dropdown" and @aria-expanded="true"]')




    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    # Методы для проверки наличия элементов
    def does_firstname_input_exist(self):
        """
        Метод для проверки наличия элемента firstname и получения его CSS стиля color
        """
        firstname_input = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.firstname_input_locator))
        return firstname_input.value_of_css_property("color")

    def does_lastname_input_exist(self):
        """
        Метод для проверки наличия элемента lastname и получения его CSS стиля color
        """
        lastname_input = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.lastname_input_locator))
        return lastname_input.value_of_css_property("color")

    def does_continue_button_exist(self):
        """
        Метод для проверки наличия элемента continue_button и получения его CSS стиля color
        """
        continue_button = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.continue_button_locator))
        return continue_button.value_of_css_property("color")

    def does_link_Privacy_Policy_exist(self):
        """
        Метод для проверки наличия элемента Privacy_Policy и получения его CSS стиля color
        """
        link_Privacy_Policy = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.link_Privacy_Policy_locator))
        return link_Privacy_Policy.value_of_css_property("color")

    def does_checkbox_Subscribe_exist(self):
        """
        Метод для проверки наличия элемента checkbox_Subscribe и получения его CSS стиля color
        """
        checkbox_Subscribe = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.checkbox_Subscribe_locator))
        return checkbox_Subscribe.value_of_css_property("color")

    def move_my_account_dropdown(self):
        """
        Метод для перехода на страницу Register
        """
        my_account_link = self._driver.find_element(By.LINK_TEXT, "My Account")
        my_account_link.click()
        time.sleep(1)
        register_link = self._driver.find_element(By.LINK_TEXT, "Register")
        register_link.click()
        time.sleep(1)

