from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CatalogPage:
    """
    Класс для работы со страницей каталог и элементами на этой странице
    """

    url = "http://localhost"

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
        self._driver.implicitly_wait(3)

    def does_sort_by_text_exist(self):
        """
        Метод для проверки наличия элемента сортировка и получения его CSS стиля color
        """
        sort_by_element = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.sort_by_text_locator))
        return sort_by_element.value_of_css_property("color")

    def does_sort_by_dropdown_exist(self):
        """
        Метод для проверки наличия элемента Sort_by и получения его CSS стиля color
        """
        sort_by_dropdown = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.sort_by_dropdown_locator))
        return sort_by_dropdown.value_of_css_property("color")

    def does_limit_dropdown_exist(self):
        """
        Метод для проверки наличия элемента Show и получения его CSS стиля color
        """
        limit_dropdown = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.limit_dropdown_locator))
        return limit_dropdown.value_of_css_property("color")

    def does_compare_button_exist(self):
        """
        Метод для проверки наличия элемента Сравнение и получения его CSS стиля color
        """
        compare_button = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.compare_button_locator))
        return compare_button.value_of_css_property("color")

    def does_button_list_exist(self):
        """
        Метод для проверки наличия элемента положение Лист и получения его CSS стиля color
        """
        button_list = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.button_list_locator))
        return button_list.value_of_css_property("color")

    def move_phones_link(self):
        """
        Метод для перехода с главной страницы и до католога
        """
        phones_link = self._driver.find_element(By.LINK_TEXT, "Phones & PDAs")
        phones_link.click()

        time.sleep(2)
