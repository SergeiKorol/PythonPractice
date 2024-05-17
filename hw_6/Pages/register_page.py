# Поле ввода First Name //div/input[@placeholder="First Name"]
# Поле ввода Last Name //div/input[@placeholder="Last Name"]
# Кнопка Continue //div[@class="text-end"]/button
# Ссылка на Privacy Policy //div[@class="text-end"]/div/label
# Чекбокс Subscribe //div/input[@type="checkbox"]

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    url = "http://localhost/index.php?route=account/register"

    # Локаторы
    firstname_input_locator = (By.XPATH, '//div/input[@placeholder="First Name"]')
    lastname_input_locator = (By.XPATH, '//div/input[@placeholder="Last Name"]')
    continue_button_locator = (By.XPATH, '//div[@class="text-end"]/button')
    link_Privacy_Policy_locator = (By.XPATH, '//div[@class="text-end"]/div/label')
    checkbox_Subscribe_locator = (By.XPATH, '//div/input[@type="checkbox"]')

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    # Методы для проверки наличия элементов
    def does_firstname_input_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.firstname_input_locator))
            return True
        except:
            return False

    def does_lastname_input_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.lastname_input_locator))
            return True
        except:
            return False

    def does_continue_button_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.continue_button_locator))
            return True
        except:
            return False

    def does_link_Privacy_Policy_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.link_Privacy_Policy_locator))
            return True
        except:
            return False

    def does_checkbox_Subscribe_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.checkbox_Subscribe_locator))
            return True
        except:
            return False
