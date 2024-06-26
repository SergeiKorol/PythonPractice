from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage():
    """
    Класс для работы со страницей каталог и элементами на этой странице
    """
    url = "http://localhost/administration/"

    # Локаторы
    username_input_locator = (By.ID, 'input-username')
    password_input_locator = (By.ID, 'input-password')
    login_button_locator = (By.TAG_NAME, 'button')
    promo_link_locator = (By.XPATH, '//footer/a')
    data_input_form_locator = (By.XPATH, '//div[@class="card"]')

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    # Методы для проверки наличия элементов
    def does_username_input_exist(self):
        """
        Метод для проверки наличия элемента username и получения его CSS стиля color
        """
        username = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.username_input_locator))
        return username.value_of_css_property("color")

    def does_password_input_exist(self):
        """
        Метод для проверки наличия элемента password и получения его CSS стиля color
        """
        password = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.password_input_locator))
        return password.value_of_css_property("color")

    def does_login_button_exist(self):
        """
        Метод для проверки наличия элемента login_button и получения его CSS стиля color
        """
        login_button = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.login_button_locator))
        return login_button.value_of_css_property("color")

    def does_promo_link_exist(self):
        """
        Метод для проверки наличия элемента promo_link и получения его CSS стиля color
        """
        promo_link = WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.promo_link_locator))
        return promo_link.value_of_css_property("color")

    def does_data_input_form_exist(self):
        """
        Метод для проверки наличия элемента data_input_form и получения его CSS стиля color
        """
        data_input = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_element_located(self.data_input_form_locator))
        return data_input.value_of_css_property("color")
