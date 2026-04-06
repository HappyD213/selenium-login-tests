from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from elements.button import Button
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    USER_CONTAINER = "//div[contains(@class,'figure')][{}]"
    USER_NAME = "//div[contains(@class, 'figcaption')]//h5[{}]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.name = "Hovers Page"

        self.unique_element = WebElement(self.browser, self.USER_CONTAINER, description="Hovers Page -> Unique Element")
        self.user_containers = MultiWebElement(self.browser, self.USER_CONTAINER)
        self.user_names = MultiWebElement(self.browser, self.USER_NAME)

    #def check_users(self) -> None:
        #for user_container in self.user_containers:
            #ActionChains(self.browser.driver) \
                #.move_to_element(user_container.wait_for_visible()) \
                #.perform()


