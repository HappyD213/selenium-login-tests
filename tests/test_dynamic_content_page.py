from pages.dynamic_content_page import DynamicContentPage
from config.config import Config


def test_dynamic_content_page(browser):
    browser.get(Config.DYNAMIC_CONTENT_URL)
    page = DynamicContentPage(browser)
    page.wait_for_open()

    max_attempts = 10

    for _ in range(max_attempts):

        if page.is_duplicate_image():
            found = True
            break

        browser.refresh()
        page.wait_for_open()
