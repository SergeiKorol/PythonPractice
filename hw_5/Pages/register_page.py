from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RegisterPage:
    url = "http://localhost"
    #url = "http://localhost/index.php?route=account/register"

    # Локаторы
    firstname_input_locator = (By.XPATH, '//div/input[@placeholder="First Name"]')
    lastname_input_locator = (By.XPATH, '//div/input[@placeholder="Last Name"]')
    #continue_button_locator = (By.XPATH, '//div[@class="text-end"]/button')
    link_Privacy_Policy_locator = (By.XPATH, '//div[@class="text-end"]/div/label')
    checkbox_Subscribe_locator = (By.XPATH, '//div/input[@type="checkbox"]')
    #my_account_locator = (By.CSS_SELECTOR, '.d-none d-md-inline')
    #my_account_locator = (By.XPATH, "//li/div/a[@class='dropdown-toggle']")
    # my_account_locator = (By.CSS_SELECTOR, 'a.dropdown - toggle[data - bs - toggle = "dropdown"]')
    # my_account_locator = (By.LINK_TEXT, "My Account")
    # my_account_locator = (By.XPATH,'//a[@class="dropdown-toggle" and @data-bs-toggle="dropdown"]')
    my_account_locator = (By.XPATH, "//a[contains(@href,'route=account/account')]")
    continue_button_locator = (By.XPATH, "//button[@type='submit']")
    register_locator = (By.XPATH, '//a[@class="dropdown-toggle show" and @data-bs-toggle="dropdown" and @aria-expanded="true"]')




    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    # Методы для проверки наличия элементов
    def does_firstname_input_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.firstname_input_locator))
            return True
        except Exception as e:
            return e

    def does_lastname_input_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.lastname_input_locator))
            return True
        except Exception as e:
            return e

    def does_continue_button_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.continue_button_locator))
            return True
        except Exception as e:
            return e

    def does_link_Privacy_Policy_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.link_Privacy_Policy_locator))
            return True
        except Exception as e:
            return e

    def does_checkbox_Subscribe_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.checkbox_Subscribe_locator))
            return True
        except Exception as e:
            return e

    def move_my_account_dropdown(self):
        self._driver.implicitly_wait(10)
        my_account_link = self._driver.find_element(By.LINK_TEXT, "My Account")
        my_account_link.click()
        self._driver.implicitly_wait(10)
        time.sleep(3)
        self._driver.implicitly_wait(10)
        register_link = self._driver.find_element(By.LINK_TEXT, "Register")
        register_link.click()
        self._driver.implicitly_wait(10)
        time.sleep(3)

