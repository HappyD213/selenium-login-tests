from browser.browser import Browser
from elements.web_element import WebElement
from pages.base_page import BasePage


class BasicAuthenticationPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//p"
    RESULT_TEXT_LOC = "//*[@id='content']//p"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Basic Authentication Page"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Basic authentication page -> Unique element")
        self.result_text_element = WebElement(self.browser, self.RESULT_TEXT_LOC,
                                              description="Basic authentication page -> Result Text Element")

    def get_result_text(self) -> str:
        text = self.result_text_element.get_text()
        return text
