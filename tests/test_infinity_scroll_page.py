from pages.infinity_scroll_page import InfinityScrollPage
from config.config_reader import ConfigReader


def test_infinity_scroll_page(browser):
    browser.get(ConfigReader.get_infinity_scroll_page_url())
    infinity_scroll_page = InfinityScrollPage(browser)
    infinity_scroll_page.wait_for_open()

    count_to_check = 18
    infinity_scroll_page.wait_for_n_paragraphs_count(count_to_check)
