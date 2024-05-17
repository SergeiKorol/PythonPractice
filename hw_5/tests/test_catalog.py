from selenium import webdriver
from Pages.catalog_components import CatalogPage

driver = webdriver.Chrome()
catalog_page = CatalogPage(driver)


def test_sort_by_text():
    catalog_page.move_phones_link()
    assert catalog_page.does_sort_by_text_exist()


def test_ssort_by_dropdown():
    catalog_page.move_phones_link()
    assert catalog_page.does_sort_by_dropdown_exist()


def test_limit_dropdown():
    catalog_page.move_phones_link()
    assert catalog_page.does_limit_dropdown_exist()


def test_compare_button():
    catalog_page.move_phones_link()
    assert catalog_page.does_compare_button_exist()


def test_button_list():
    catalog_page.move_phones_link()
    assert catalog_page.does_button_list_exist()
