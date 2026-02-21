from pages.basic_authentication_page import BasicAuthenticationPage
from utils.config_reader import ConfigReader

config = ConfigReader()


def test_basic_authentication_page(browser):
    browser.get(config.get("DEFAULT", "base_url"))

    basic_authentication_page = BasicAuthenticationPage(browser)
    basic_authentication_page.wait_for_opening()

    expected_text = "Congratulations! You must have the proper credentials."
    actual_text = basic_authentication_page.get_element_text()

    assert expected_text in actual_text, f"Expected to find: {expected_text} but actual text was: {actual_text}"