# 1 Поле поиск $$('[name="search"]')
# 2 Выпадашка по категориям $$('.fa-solid.fa-bars')
# 3 Кнопка с итого $$('button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle.show')
# 4 Футтер $$('footer')
# 5 Значёк избранное $$('#wishlist-total')
# 6 Выпадашка с валютой $$('[data-popper-placement="bottom-start"]')
# xpath
# Имя вкладки //head/title
# Валюта выбранная по умолчанию//a[@class="dropdown-toggle"]/strong


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    url = "http://localhost"
    search_field_locator = (By.CSS_SELECTOR, '[name="search"]')
    category_dropdown_locator = (By.CSS_SELECTOR, '.fa-solid.fa-bars')
    button_total_locator = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle.show')
    footer_locator = (By.CSS_SELECTOR, 'footer')
    wishlist_locator = (By.CSS_SELECTOR, '#wishlist-total')
    currency_dropdown_locator = (By.CSS_SELECTOR, '[data-popper-placement="bottom-start"]')

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    def does_search_field_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.search_field_locator))
            return True
        except:
            return False

    def does_category_dropdown_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.category_dropdown_locator))
            return True
        except:
            return False

    def does_button_total_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.button_total_locator))
            return True
        except:
            return False

    def does_footer_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.footer_locator))
            return True
        except:
            return False

    def does_wishlist_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.wishlist_locator))
            return True
        except:
            return False

    def does_currency_dropdown_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.currency_dropdown_locator))
            return True
        except:
            return False
