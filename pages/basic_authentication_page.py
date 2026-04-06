from browser.browser import Browser
from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage


class BasicAuthenticationPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//p"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.name = "Basic Authentication Page"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, description="Basic authentication page -> Unique element")

    def get_result_text(self) -> str:
        Logger.info(f"{self}: get_result_text")
        text = self.unique_element.get_text()
        return text
