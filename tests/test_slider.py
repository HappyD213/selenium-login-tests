from config.config_reader import ConfigReader
from pages.slider_page import SliderPage

config = ConfigReader()


def test_slider_move(browser):
    browser.get(config.get("DEFAULT", "slider_url"))
    slider_page = SliderPage(browser)
    slider_page.wait_for_open()

    value_for_test = 5
    slider_page.set_slider_value(value_for_test)
    actual_result_text = slider_page.get_result_text()
    expected_result_text = str(value_for_test)
    assert actual_result_text == expected_result_text, f"Expected: {expected_result_text} != Actual: {actual_result_text}"