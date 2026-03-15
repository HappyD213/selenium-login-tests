from utils.config_reader import ConfigReader
from pages.slider_page import SliderPage

config = ConfigReader()


def test_slider_move(browser):
    browser.get(config.get("DEFAULT", "slider_url"))
    slider_page = SliderPage(browser)
    slider_page.wait_for_displayed()

    expected_value = slider_page.move_slider()
    actual_value = slider_page.get_current_value()
    assert expected_value == actual_value, (f"Expected not equal to actual\n"
                                            f"Actual value: {actual_value}\n"
                                            f"Expected value: {expected_value}")
