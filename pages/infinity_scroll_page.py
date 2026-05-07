from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "(//div[contains(@class, 'jscroll-added')])[1]"
    PARAGRAPHS_LOC = "(//div[contains(@class, 'jscroll-added')])[{}]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Infinity Scroll Page"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Infinity Scroll Page -> Unique Element")
        self.paragraphs = MultiWebElement(self.browser, self.PARAGRAPHS_LOC,
                                          description="Infinity Scroll Page -> Paragraphs")

    def wait_for_n_paragraphs_count(self, count_to_check: int):
        counter = 0
        while counter != count_to_check:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            counter = self.paragraphs.count()
