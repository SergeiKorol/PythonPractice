from selenium import webdriver
from hw_5.Pages.component_monitor import MonitorPage

driver = webdriver.Chrome()
monitor_page = MonitorPage(driver)


def test_item_name():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(68, 68, 68, 1)'
    monitor_page.move_to_monitor()
    assert monitor_page.does_item_name_exist() == expected_css


def test_item_price():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(68, 68, 68, 1)'
    monitor_page.move_to_monitor()
    assert monitor_page.does_item_price_exist() == expected_css


def test_upload_button():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(119, 119, 119, 1)'
    monitor_page.move_to_monitor()
    assert monitor_page.does_upload_button_exist() == expected_css


def test_textarea():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(33, 37, 41, 1)'
    monitor_page.move_to_monitor()
    assert monitor_page.does_textarea_exist() == expected_css


def test_text_Available_Options():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(68, 68, 68, 1)'
    monitor_page.move_to_monitor()
    assert monitor_page.does_text_Available_Options_exist() == expected_css


def test_add_to_cart_button():
    """
    Тест проверяет что CSS стиль color соответствует ожидаемому в переменной expected_css
    """
    expected_css = 'rgba(255, 255, 255, 1)'
    monitor_page.move_to_monitor()
    assert monitor_page.does_add_to_cart_button_exist() == expected_css
