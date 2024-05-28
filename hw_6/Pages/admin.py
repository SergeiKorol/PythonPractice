from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver


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
    catalog_locator = (By.XPATH, '//a[@href="#collapse-1" and contains(@class, "parent") and contains(@class, "collapsed")]')
    product_locator =(By.XPATH, '//a[contains(@href, "route=catalog/product")]')
    #add_new_locator = (By.XPATH, '//a[contains(@aria-label, "Add New") and contains(@href, "route=catalog/option.form")]')
    #add_new_locator = (By.XPATH, '//a[contains(@aria-label, "Add New") and contains(@class, "btn btn-primary")]')
    #add_new_locator = (By.XPATH, '//div[@id="content"]//a[@aria-label="Add New" and contains(@class, "btn btn-primary")]')
    add_new_locator =(By.CSS_SELECTOR, ".fa-plus")
    #//li[@id ="menu-catalog"]/a
    product_name_locator = (By.ID, 'input-name-1')
    meta_title_locator = (By.ID, 'input-meta-title-1')
    data_tab_locator = (By.XPATH, '//a[contains(text(), "Data")]')
    model_locator = (By.ID, 'input-model')
    button_save_locator = (By.XPATH, '//button[@type="submit"]')
    seo_tab_locator = (By.XPATH, '//a[contains(text(), "SEO")and @role="tab"]')
    seo_text_locator = (By.ID, 'input-keyword-0-1')
    #back_button_locator = (By.XPATH, '//a[contains(@aria-label, "Back")]')
    back_button_locator = (By.XPATH, '//div[@class="float-end"]/a')
    column_quantity_locator= (By.XPATH, '//a[contains(text(), "Quantity")]')
    rows_in_tab = (By.XPATH, '//tbody/tr')
    alert_button_locator = (By.XPATH, '//button[@type="button"]')
    logout_button_lockator = (By.XPATH,'//li[@id="nav-logout"]/a')
    new_product_checkbox_locator = (By.XPATH, '//tbody/tr[2]/td[1]')
    delete_button_lockator =(By.CSS_SELECTOR, ".fa-trash-can")

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.url)

    def username_input(self):
        """
        Метод заполнения username
        """
        username_input = self._driver.find_element(By.ID, 'input-username')
        username_input.clear()
        username_input.send_keys('user')


    def password_input(self):
        """
        Метод заполнения password
        """
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.password_input_locator))
        password = self._driver.find_element(*self.password_input_locator)
        password.clear()
        password.send_keys("bitnami")

    def login_button_click(self):
        """
        Метод жмём по кнопке login
        """
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.password_input_locator))
        button = self._driver.find_element(By.TAG_NAME, 'button')
        button.click()


    def move_to_addNew_product(self):
        """
        Метод перехода к странице создания товара
        """
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.catalog_locator))
        self._driver.find_element(*self.catalog_locator).click()

        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.product_locator))
        self._driver.find_element(*self.product_locator).click()


    def add_new_click(self):
        WebDriverWait(self._driver, 5).until(EC.visibility_of_element_located(self.add_new_locator))
        self._driver.find_element(*self.add_new_locator).click()

    def make_new_product(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.product_name_locator))
        product_name = self._driver.find_element(*self.product_name_locator)
        product_name.clear()
        product_name.send_keys("Test Product_1")

        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.meta_title_locator))
        meta_title = self._driver.find_element(*self.meta_title_locator)
        meta_title.clear()
        meta_title.send_keys("Test Product_meta")

        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.data_tab_locator))
        self._driver.find_element(*self.data_tab_locator).click()

        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.model_locator))
        model = self._driver.find_element(*self.model_locator)
        model.clear()
        model.send_keys("Test Product_model")

        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.seo_tab_locator))
        self._driver.find_element(*self.seo_tab_locator).click()


        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.seo_text_locator))
        seo_text = self._driver.find_element(*self.seo_text_locator)
        seo_text.clear()
        seo_text.send_keys("Test_Product_seo_text")

        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.button_save_locator))
        self._driver.find_element(*self.button_save_locator).click()

    def back_button_click(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.alert_button_locator))
        self._driver.find_element(*self.alert_button_locator).click()
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.back_button_locator))
        self._driver.find_element(*self.back_button_locator).click()


    def sort_by_quantity(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.column_quantity_locator))
        self._driver.find_element(*self.column_quantity_locator).click()
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.column_quantity_locator))
        self._driver.find_element(*self.column_quantity_locator).click()

    def check_product_in_table(self):
        rows = WebDriverWait(self._driver, 2).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr'))
        )
        product_names = []
        for row in rows:
            # Найти ячейку с именем продукта в текущей строке
            product_name_cell = row.find_element(By.XPATH, './td[3]')
            # Получить полный текст ячейки
            full_text = product_name_cell.text
            # Извлечь имя продукта, исключая все после '\n'
            product_name = full_text.split('\n')[0].strip()
            # Добавить имя продукта в список
            product_names.append(product_name)



        product_found = False
        for row in product_names:

            if "Test Product_1" in product_names:
                product_found = True
                break
        return product_found

    def click_logout(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.logout_button_lockator))
        self._driver.find_element(*self.logout_button_lockator).click()

    def checkbox_click(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.new_product_checkbox_locator))
        self._driver.find_element(*self.new_product_checkbox_locator).click()

    def alert_click(self):
        self._driver.switch_to.alert.accept()

    def delete_button_click(self):
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(self.delete_button_lockator))
        self._driver.find_element(*self.delete_button_lockator).click()
