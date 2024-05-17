# http://localhost/en-gb/catalog/smartphone
# Указатель сортировать по //div/label[@for="input-sort"]
# Выпадашка сортировать по //div/select[@id="input-sort"]
# Выпадашка показать сколько //div/select[@id="input-limit"]
# Кнопка сравнить //a[@id="compare-total"]/i
# Кнопка показать списком //div/button[@id="button-list"]/i


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage:
    url = "http://localhost/en-gb/catalog/smartphone"

    # Локаторы
    sort_by_text_locator = (By.XPATH, '//div/label[@for="input-sort"]')
    sort_by_dropdown_locator = (By.XPATH, '//div/select[@id="input-sort"]')
    limit_dropdown_locator = (By.XPATH, '//div/select[@id="input-limit"]')
    compare_button_locator = (By.XPATH, '//a[@id="compare-total"]/i')
    button_list_locator = (By.XPATH, '//div/button[@id="button-list"]/i')

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    # Методы для проверки наличия элементов
    def does_sort_by_text_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.sort_by_text_locator))
            return True
        except:
            return False

    def does_sort_by_dropdown_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.sort_by_dropdown_locator))
            return True
        except:
            return False

    def does_limit_dropdown_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.limit_dropdown_locator))
            return True
        except:
            return False

    def does_compare_button_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.compare_button_locator))
            return True
        except:
            return False

    def does_button_list_exist(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.button_list_locator))
            return True
        except:
            return False
