
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class AdminPage:
    url = "http://localhost/administration/"

    # Локаторы
    username_input_locator = (By.XPATH, '//div/input[@id="input-username"]')
    password_input_locator = (By.XPATH, '//div/input[@id="input-password"]')
    login_button_locator = (By.XPATH, '//button')
    catalog_link_locator = (By.XPATH, "//a[contains(text(), 'Catalog')]")
    products_link_locator = (By.XPATH, "//ul[@id='collapse-1']//a[text()='Products']")

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    # Методы для проверки наличия элементов
    def username_input(self):
        username_input = self._driver.find_element(By.XPATH, '//div/input[@id="input-username"]')
        username_input.clear()
        username_input.send_keys("user")
        time.sleep(2)

    def password_input(self):
        password_input = self._driver.find_element(By.XPATH, '//div/input[@id="input-password"]')
        password_input.clear()
        password_input.send_keys("bitnami")
        time.sleep(2)

    def login_button_click(self):
        self._driver.find_element(By.XPATH, '//button').click()
        time.sleep(5)

    def catalog_click(self):
        self._driver.find_element(By.XPATH, "//a[@href='#collapse-1']").click()
        time.sleep(2)

    def products_click(self):
        self._driver.find_element(By.XPATH, "//ul[@id='collapse-1']//a[text()='Products']").click()
        time.sleep(2)



    # def move_phones_link(self):
    #     self._driver.implicitly_wait(10)
    #     phones_link = self._driver.find_element(By.LINK_TEXT, "Phones & PDAs")
    #     phones_link.click()
    #     self._driver.implicitly_wait(10)
    #     time.sleep(3)