from pages.infinity_scroll_page import InfinityScrollPage
from config.config import Config


def test_infinity_scroll_page(browser):
    browser.get(Config.INFINITY_SCROLL_PAGE)
    infinity_scroll_page = InfinityScrollPage(browser)
    infinity_scroll_page.wait_for_open()

    count_to_check = 18
    infinity_scroll_page.wait_for_n_paragraphs_count(count_to_check)
