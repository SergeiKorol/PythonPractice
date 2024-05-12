# Поле ввода username //div/input[@id="input-username"]
# Поле ввода password //div/input[@id="input-password"]
# Единственная кнопка  login //button
# Ссылка на промо //footer/a
# форма для ввода данных //div[@class="card"]

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    url = "http://localhost/administration/"

    # Локаторы
    username_input_locator = (By.XPATH, '//div/input[@id="input-username"]')
    password_input_locator = (By.XPATH, '//div/input[@id="input-password"]')
    login_button_locator = (By.XPATH, '//button')
    promo_link_locator = (By.XPATH, '//footer/a')
    data_input_form_locator = (By.XPATH, '//div[@class="card"]')

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    # Методы для проверки наличия элементов
    def does_username_input_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.username_input_locator))
            return True
        except:
            return False

    def does_password_input_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.password_input_locator))
            return True
        except:
            return False

    def does_login_button_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.login_button_locator))
            return True
        except:
            return False

    def does_promo_link_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.promo_link_locator))
            return True
        except:
            return False

    def does_data_input_form_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.data_input_form_locator))
            return True
        except:
            return False
