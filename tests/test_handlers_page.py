from pages.handlers_page import HandlersPage
from pages.handlers_new_window_page import NewWindowPage
from config.config import Config


def test_handlers_page(browser):
    browser.get(Config.HANDLERS_URL)
    handlers_page = HandlersPage(browser)
    handlers_page.wait_for_open()

    current_handles = browser.get_current_window_handles()
    handlers_page.click_new_window_button()
    browser.new_window_to_be_available_and_switch_to_it(current_handles)

    new_window_page = NewWindowPage(browser)
    new_window_page.wait_for_open()
    expected_text = "New Window"
    actual_text = new_window_page.get_result_text()
    assert expected_text in actual_text, f"{expected_text} != {actual_text}"

    expected_title = "New Window"
    actual_title = browser.get_current_title()
    assert expected_title in actual_title, f"{expected_title} != {actual_title}"

    browser.back()
    browser.switch_to_default_window()
    handlers_page.wait_for_open()

    current_handles = browser.get_current_window_handles()
    handlers_page.click_new_window_button()
    browser.new_window_to_be_available_and_switch_to_it(current_handles)

    new_window_page.wait_for_open()
    expected_text = "New Window"
    actual_text = new_window_page.get_result_text()
    assert expected_text in actual_text, f"{expected_text} != {actual_text}"

    expected_title = "New Window"
    actual_title = browser.get_current_title()
    assert expected_title in actual_title, f"{expected_title} != {actual_title}"

    browser.back()
    browser.switch_to_default_window()
    handlers_page.wait_for_open()

    title_to_close = 'New Window'
    browser.switch_to_window(title_to_close)
    browser.close()
    browser.switch_to_window(title_to_close)
    browser.close()
