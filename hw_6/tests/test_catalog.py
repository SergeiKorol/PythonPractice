from selenium import webdriver
from hw_6.Pages.catalog_components import CatalogPage

driver = webdriver.Chrome()
catalog_page = CatalogPage(driver)


def test_sort_by_text():
    assert catalog_page.does_sort_by_text_exist()


def test_ssort_by_dropdown():
    assert catalog_page.does_sort_by_dropdown_exist()


def test_limit_dropdown():
    assert catalog_page.does_limit_dropdown_exist()


def test_compare_button():
    assert catalog_page.does_compare_button_exist()


def test_button_list():
    assert catalog_page.does_button_list_exist()
