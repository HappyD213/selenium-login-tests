from config.config import Config
from pages.slider_page import SliderPage


def test_slider_move(browser):
    browser.get(Config.SLIDER_URL)
    slider_page = SliderPage(browser)
    slider_page.wait_for_open()

    slider_min_value = slider_page.get_min_slider_value()
    slider_max_value = slider_page.get_max_slider_value()
    slider_step = slider_page.get_slider_step()

    value_for_test = slider_page.generate_random_values_for_slider(slider_min_value, slider_max_value, slider_step)
    slider_page.set_slider_value(value_for_test)
    actual_result_text = slider_page.get_result_text()
    expected_result_text = value_for_test
    assert actual_result_text == expected_result_text, (f"Expected: {expected_result_text} != "
                                                        f"Actual: {actual_result_text}")
