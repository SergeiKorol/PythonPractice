from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
        Класс для работы с главной страницей и элементами на этой странице
    """
    url = "http://localhost"
    search_field_locator = (By.CSS_SELECTOR, '[name="search"]')
    desktop_locator = (By.XPATH, "//a[@href='http://localhost/en-gb/catalog/desktops' and contains(@class, 'nav-link') and contains(@class, 'dropdown-toggle')]")
    category_dropdown_locator = (By.CSS_SELECTOR, '.fa-solid.fa-bars')
    featured_locator = (By.XPATH, '//h3')
    footer_locator = (By.TAG_NAME, 'footer')
    wishlist_locator = (By.ID, 'wishlist-total')
    currency_dropdown_locator = (By.CSS_SELECTOR, '[data-popper-placement="bottom-start"]')
    opencart_locator = (By.XPATH, "//img[contains(@src, 'opencart-logo.png') and @title='Your Store' and @alt='Your Store']")
    opencart_link_locator = (By.XPATH,"// a[ @ href = 'https://www.opencart.com']")

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    def does_search_field_exist(self):
        """
        Метод для проверки наличия элемента поиск и получения его CSS стиля color
        """
        search_field = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.search_field_locator))
        return search_field.value_of_css_property("color")

    def does_opencart_exist(self):
        """
        Метод для проверки наличия главной ссылки opencart и получения его CSS стиля color
        """
        opencart = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.opencart_locator))
        return opencart.value_of_css_property("color")

    def does_featured_exist(self):
        """
        Метод для проверки наличия ссылки opencart и получения его CSS стиля color
        """
        featured = WebDriverWait(self._driver, 3).until(EC.visibility_of_element_located(self.featured_locator))
        return featured.value_of_css_property("color")

    def does_footer_exist(self):
        """
        Метод для проверки наличия footer и получения его CSS стиля color
        """
        footer = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.footer_locator))
        return footer.value_of_css_property("color")

    def does_wishlist_exist(self):
        """
        Метод для проверки наличия кнопки wishlist и получения его CSS стиля color
        """
        wishlist = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.wishlist_locator))
        return wishlist.value_of_css_property("color")

    def does_opencart_link_exist(self):
        """
        Метод для проверки наличия ссылки opencart в футтере и получения его CSS стиля color
        """
        opencart_link = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.opencart_link_locator))
        return opencart_link.value_of_css_property("color")
