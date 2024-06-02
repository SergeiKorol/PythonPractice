from selenium import webdriver
from hw_5.Pages.catalog_components import CatalogPage

driver = webdriver.Chrome()
catalog_page = CatalogPage(driver)


def test_sort_by_text():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    catalog_page.move_phones_link()
    assert catalog_page.does_sort_by_text_exist() == expected_css


def test_ssort_by_dropdown():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    catalog_page.move_phones_link()
    assert catalog_page.does_sort_by_dropdown_exist() == expected_css


def test_limit_dropdown():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    catalog_page.move_phones_link()
    assert catalog_page.does_limit_dropdown_exist() == expected_css


def test_compare_button():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(255, 255, 255, 1)'
    catalog_page.move_phones_link()
    assert catalog_page.does_compare_button_exist() == expected_css


def test_button_list():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(119, 119, 119, 1)'
    catalog_page.move_phones_link()
    assert catalog_page.does_button_list_exist() == expected_css
