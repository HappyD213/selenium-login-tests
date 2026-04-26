from elements.web_element import WebElement
from pages.base_page import BasePage
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3"
    TEXT_ELEMENT_LOC = "//h3"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "New Window Page"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Handlers New Window Page -> Unique Element")
        self.text_element = WebElement(self.browser, self.TEXT_ELEMENT_LOC,
                                       description="Handlers New Window Page -> Text Element")

    def get_result_text(self) -> str:
        text = self.text_element.get_text()
        return text
