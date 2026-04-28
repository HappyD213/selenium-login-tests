from pages.base_page import BasePage
from elements.web_element import WebElement
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser


class NestedPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h1[contains(text(), 'Nested Frames')]"
    NESTED_PARENT_FRAME_LOC = "frame1"
    NESTED_PARENT_TEXT_LOC = "//body"
    NESTED_CHILD_FRAME_LOC = "//iframe"
    NESTED_CHILD_TEXT_LOC = "//p"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Nested Frames"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Nested Frames Page -> Unique element")
        self.nested_parent = WebElement(self.browser, self.NESTED_PARENT_FRAME_LOC,
                                        description="Iframe Page -> Nested Parent Element")
        self.nested_child = WebElement(self.browser, self.NESTED_CHILD_FRAME_LOC,
                                       description="Iframe Page -> Nested Child Element")
        self.nested_parent_text = WebElement(self.browser, self.NESTED_PARENT_TEXT_LOC,
                                             description="Iframe Page -> Nested Parent Text")
        self.nested_child_text = WebElement(self.browser, self.NESTED_CHILD_TEXT_LOC,
                                            description="Iframe Page -> Nested Child Text")

    def get_parent_frame_text(self) -> str:
        self.browser.switch_to_frame(self.nested_parent)
        text = self.nested_parent_text.get_text()
        self.browser.switch_to_default_content()
        return text

    def get_child_frame_text(self) -> str:
        self.browser.switch_to_frame(self.nested_parent)
        self.browser.switch_to_frame(self.nested_child)
        text = self.nested_child_text.get_text()
        self.browser.switch_to_default_content()
        return text
