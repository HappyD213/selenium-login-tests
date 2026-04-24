from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser


class HandlersPage(BasePage):
    HANDLERS_PAGE_UNIQUE_LOC = "//div[contains(@class, 'example')]//a"
    OPEN_NEW_WINDOW_BUTTON = "//div[contains(@class, 'example')]//a"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.name = "Handlers Page"

        self.unique_element = WebElement(self.browser, self.HANDLERS_PAGE_UNIQUE_LOC,
                                         description=f"Handlers Page -> Unique Element")
        self.new_window_button = Button(self.browser, self.OPEN_NEW_WINDOW_BUTTON,
                                        description=f"Handlers Page -> New Window Button")

    def click_new_window_button(self):
        self.new_window_button.click()
