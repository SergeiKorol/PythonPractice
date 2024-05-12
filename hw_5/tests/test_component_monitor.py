from selenium import webdriver
from Pages.admin import MonitorPage

driver = webdriver.Chrome()
monitor_page = MonitorPage(driver)


def test_item_name():
    assert monitor_page.does_item_name_exist()


def test_item_price():
    assert monitor_page.does_item_price_exist()


def test_wishlist_button():
    assert monitor_page.does_wishlist_button_exist()


def test_compare_button():
    assert monitor_page.does_compare_button_exist()


def test_text_Available_Options():
    assert monitor_page.does_text_Available_Options_exist()


def test_add_to_cart_button():
    assert monitor_page.does_add_to_cart_button_exist()
