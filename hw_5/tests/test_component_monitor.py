from selenium import webdriver
from Pages.component_monitor import MonitorPage

driver = webdriver.Chrome()
monitor_page = MonitorPage(driver)


def test_item_name():
    monitor_page.move_to_monitor()
    assert monitor_page.does_item_name_exist()


def test_item_price():
    monitor_page.move_to_monitor()
    assert monitor_page.does_item_price_exist()


def test_wishlist_button():
    monitor_page.move_to_monitor()
    assert monitor_page.does_wishlist_button_exist()


def test_compare_button():
    monitor_page.move_to_monitor()
    assert monitor_page.does_compare_button_exist()


def test_text_Available_Options():
    monitor_page.move_to_monitor()
    assert monitor_page.does_text_Available_Options_exist()


def test_add_to_cart_button():
    monitor_page.move_to_monitor()
    assert monitor_page.does_add_to_cart_button_exist()
