from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    url = "http://localhost"
    search_field_locator = (By.CSS_SELECTOR, '[name="search"]')
    category_dropdown_locator = (By.CSS_SELECTOR, '.fa-solid.fa-bars')
    button_total_locator = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle.show')
    footer_locator = (By.TAG_NAME, 'footer')
    wishlist_locator = (By.ID, 'wishlist-total')
    currency_dropdown_locator = (By.CSS_SELECTOR, '[data-popper-placement="bottom-start"]')

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    def does_search_field_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.search_field_locator))
            return True
        except Exception as e:
            return e

    def does_category_dropdown_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.category_dropdown_locator))
            return True
        except Exception as e:
            return e

    def does_button_total_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.button_total_locator))
            return True
        except Exception as e:
            return e

    def does_footer_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.footer_locator))
            return True
        except Exception as e:
            return e

    def does_wishlist_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.wishlist_locator))
            return True
        except Exception as e:
            return e

    def does_currency_dropdown_exist(self):
        try:
            WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.currency_dropdown_locator))
            return True
        except Exception as e:
            return e
