from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MonitorPage:
    """
    Класс для работы со страницей одного из товаров монитор и элементами на этой странице
    """
    url = "http://localhost"

    # Локаторы
    item_name_locator = (By.XPATH, '//h1')
    item_price_locator = (By.XPATH, '//h2/span[@class="price-new"]')
    wishlist_button_locator = (By.CSS_SELECTOR, "button[aria-label='Add to Wish List']")
    upload_button_locator = (By.ID, "button-upload-222")
    textarea_locator = (By.ID, "input-option-209")
    compare_button_locator = (By.CSS_SELECTOR, "button[aria-label='Compare this Product']")
    text_Available_Options_locator = (By.XPATH, '//div[@id="product"]/form/h3')
    add_to_cart_button_locator = (By.XPATH, '//button[@id="button-cart"]')

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    def does_item_name_exist(self):
        """
        Метод для проверки наличия элемента с именем товара и получения его CSS стиля color
        """
        item_name = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.item_name_locator))
        return item_name.value_of_css_property("color")

    def does_item_price_exist(self):
        """
        Метод для проверки наличия элемента с ценой товара и получения его CSS стиля color
        """
        item_price = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.item_price_locator))
        return item_price.value_of_css_property("color")

    def does_upload_button_exist(self):
        """
        Метод для проверки наличия элемента для загрузки картинки товара и получения его CSS стиля color
        """
        upload_button = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.upload_button_locator))
        return upload_button.value_of_css_property("color")

    def does_textarea_exist(self):
        """
        Метод для проверки наличия элемента для описания товара и получения его CSS стиля color
        """
        textarea = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.textarea_locator))
        return textarea.value_of_css_property("color")

    def does_text_Available_Options_exist(self):
        """
        Метод для проверки наличия элемента для описания Available_Options товара и получения его CSS стиля color
        """
        text_Available_Options = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.text_Available_Options_locator))
        return text_Available_Options.value_of_css_property("color")

    def does_add_to_cart_button_exist(self):
        """
        Метод для проверки наличия элемента добавления в корзину товара и получения его CSS стиля color
        """
        add_to_cart_button = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.add_to_cart_button_locator))
        return add_to_cart_button.value_of_css_property("color")

    def move_to_monitor(self):
        """
        Метод для перехода из главной страницы в описание конкретного товара монитор
        """
        components_link = self._driver.find_element(By.LINK_TEXT, "Components")
        components_link.click()
        time.sleep(1)
        monitors_link = self._driver.find_element(By.LINK_TEXT, "Monitors (2)")
        monitors_link.click()
        time.sleep(1)
        apple_link = self._driver.find_element(By.LINK_TEXT, 'Apple Cinema 30"')
        apple_link.click()
