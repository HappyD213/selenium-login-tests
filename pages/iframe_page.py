from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.button import Button
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser


class IFramePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//a[contains(@href, 'demoqa.com')]"
    NESTED_FRAMES_BUTTON_LOC = "//a[contains(@href, '/nestedframes')]"
    FRAMES_PAGE_LOC = "//a[contains(@href, '/frames')]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "IFrame Page"

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Iframe Page -> Unique element")
        self.nested_frames_button = Button(browser, self.NESTED_FRAMES_BUTTON_LOC,
                                           description="Iframe Page -> Nested Frame Button")
        self.frames_page_button = Button(browser, self.FRAMES_PAGE_LOC,
                                         description="Iframe Page -> Frames Page Button")

    def click_nested_frames_btn(self):
        self.nested_frames_button.click()

    def click_frames_page_btn(self):
        self.frames_page_button.click()
