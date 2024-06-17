from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
        Класс для работы с главной страницей и элементами на этой странице
    """
    url = "http://localhost"
    search_field_locator = (By.CSS_SELECTOR, '[name="search"]')
    desktop_locator = (By.XPATH,
                       "//a[@href='http://localhost/en-gb/catalog/desktops' and contains(@class, 'nav-link') and contains(@class, 'dropdown-toggle')]")
    category_dropdown_locator = (By.CSS_SELECTOR, '.fa-solid.fa-bars')
    featured_locator = (By.XPATH, '//h3')
    footer_locator = (By.TAG_NAME, 'footer')
    wishlist_locator = (By.ID, 'wishlist-total')
    # currency_dropdown_locator = (By.LINK_TEXT, "£ Currency")
    currency_dropdown_locator = (By.CSS_SELECTOR, "a[data-bs-toggle='dropdown']")
    pound_currency_locator = (By.LINK_TEXT, "£ Pound Sterling")
    opencart_locator = (
    By.XPATH, "//img[contains(@src, 'opencart-logo.png') and @title='Your Store' and @alt='Your Store']")
    opencart_link_locator = (By.XPATH, "// a[ @ href = 'https://www.opencart.com']")
    current_currency_locator = (By.CSS_SELECTOR, "a.dropdown-toggle strong")
    currency_list_locator = (By.CSS_SELECTOR, "ul.dropdown-menu li a.dropdown-item")

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    def currency_click(self):
        WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.currency_dropdown_locator)).click()

    def get_current_currency(self):
        current_currency_element = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.current_currency_locator)
        )

        current_currency = current_currency_element.text.strip()
        print(f"Текущая валюта: {current_currency}")

    def pick_up_currency_list(self):
        currency_list = self._driver.find_elements(By.CSS_SELECTOR, "ul.dropdown-menu li a.dropdown-item")
        print("Доступные валюты:")
        for currency in currency_list:
            currency_text = currency.text.strip()
            print(currency_text)

    def choose_another_currency(self):
        current_currency_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self.current_currency_locator)
        )
        current_currency = current_currency_element.text.strip()
        print(f"Текущая валюта: {current_currency}")

        currency_list = self._driver.find_elements(By.CSS_SELECTOR, "ul.dropdown-menu li a.dropdown-item")
        for currency in currency_list:
            currency_text = currency.text.strip()
            print(currency_text)

        for currency in currency_list:
            currency_text = currency.text.strip()
            if current_currency in currency_text:
                continue
            currency.click()
            break
