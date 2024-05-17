# Наименование товара //h1
# Цена товара без скидки //h2/span[@class="price-new"]
# Значёк добавить в избранное $$('.fa-solid fa-heart')
# Значёк сравнение //button[contains(@aria-label, "Compare this Product")]
# Заголовок Available Options //div[@id="product"]/form/h3
# Кнопка добавить в корзину //button[@id="button-cart"]

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MonitorPage:
    url = "http://localhost"
    #url = "http://localhost/en-gb/product/desktops/apple-cinema"

    # Локаторы
    item_name_locator = (By.XPATH, '//h1')
    item_price_locator = (By.XPATH, '//h2/span[@class="price-new"]')
    wishlist_button_locator = (By.CSS_SELECTOR, '.fa-solid fa-heart')
    #compare_button_locator = (By.XPATH, "//button[@aria-label='Compare this Product']")
    compare_button_locator = (By.CSS_SELECTOR, "button[aria-label='Compare this Product']")
    text_Available_Options_locator = (By.XPATH, '//div[@id="product"]/form/h3')
    add_to_cart_button_locator = (By.XPATH, '//button[@id="button-cart"]')

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    # Методы для проверки наличия элементов
    def does_item_name_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.item_name_locator))
            return True
        except:
            return False

    def does_item_price_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.item_price_locator))
            return True
        except:
            return False

    def does_wishlist_button_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.wishlist_button_locator))
            return True
        except:
            return False

    def does_compare_button_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.compare_button_locator))
            return True
        except:
            return False

    def does_text_Available_Options_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.text_Available_Options_locator))
            return True
        except:
            return False

    def does_add_to_cart_button_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.add_to_cart_button_locator))
            return True
        except:
            return False

    def move_to_monitor(self):
        self._driver.implicitly_wait(10)
        components_link = self._driver.find_element(By.LINK_TEXT, "Components")
        components_link.click()
        self._driver.implicitly_wait(10)
        time.sleep(3)
        self._driver.implicitly_wait(10)
        monitors_link = self._driver.find_element(By.LINK_TEXT, "Monitors (2)")
        monitors_link.click()
        self._driver.implicitly_wait(10)
        time.sleep(3)
        apple_link = self._driver.find_element(By.LINK_TEXT, 'Apple Cinema 30"')
        apple_link.click()
        self._driver.implicitly_wait(10)

