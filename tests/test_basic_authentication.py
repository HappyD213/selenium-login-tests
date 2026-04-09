from pages.basic_authentication_page import BasicAuthenticationPage
from config.config_reader import ConfigReader
from utils.url_builder import UrlBuilder


def test_basic_authentication_page(browser):
    browser.get(UrlBuilder.get_basic_auth_url(ConfigReader.get_base_url(), ConfigReader.get_login(),
                                              ConfigReader.get_password()))

    basic_authentication_page = BasicAuthenticationPage(browser)
    basic_authentication_page.wait_for_open()

    expected_text = "Congratulations! You must have the proper credentials."
    actual_text = basic_authentication_page.get_result_text()

    assert expected_text in actual_text, f"Expected: {expected_text} Actual: {actual_text}"
