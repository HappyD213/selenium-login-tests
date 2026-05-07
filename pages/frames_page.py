from pages.base_page import BasePage
from elements.web_element import WebElement
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h1[contains(text(), 'Frames')]"
    FRAMES_FIRST_LOC = "frame1"
    FRAMES_FIRST_TEXT_LOC = "sampleHeading"
    FRAMES_SECOND_LOC = "frame2"
    FRAMES_SECOND_TEXT_LOC = "sampleHeading"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Frames Page"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Frames Page -> Unique Element")
        self.frames_first = WebElement(self.browser, self.FRAMES_FIRST_LOC,
                                       description="frame Page -> Frames First Element")
        self.frames_second = WebElement(self.browser, self.FRAMES_SECOND_LOC,
                                        description="frame Page -> Frames Second Element"
                                        )
        self.frames_first_text = WebElement(self.browser, self.FRAMES_FIRST_TEXT_LOC,
                                            description="frame Page -> Frames First Text")
        self.frames_second_text = WebElement(self.browser, self.FRAMES_SECOND_TEXT_LOC,
                                             description="frame Page -> Frames Second Text")

    def get_first_frame_text(self) -> str:
        self.browser.switch_to_frame(self.frames_first)
        text = self.frames_first_text.get_text()
        self.browser.switch_to_default_content()
        return text

    def get_second_frame_text(self) -> str:
        self.browser.switch_to_frame(self.frames_second)
        text = self.frames_second_text.get_text()
        self.browser.switch_to_default_content()
        return text
