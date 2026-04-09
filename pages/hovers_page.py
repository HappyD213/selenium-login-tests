from typing import TYPE_CHECKING
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement

if TYPE_CHECKING:
    from browser.browser import Browser


class HoversPage(BasePage):
    HOVERS_PAGE_UNIQUE_LOC = "//div[contains(@class,'figure')]"
    USER_CONTAINERS_LOC = "//div[contains(@class,'figure')][{}]"
    USER_NAMES_LOC = "(//div[contains(@class, 'figcaption')]//h5)[{}]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.name = "Hovers Page"

        self.unique_element = WebElement(self.browser, self.HOVERS_PAGE_UNIQUE_LOC,
                                         description="Hovers Page -> Unique Element")
        self.user_containers = MultiWebElement(self.browser, self.USER_CONTAINERS_LOC,
                                               description="Hovers Page -> User Containers")
        self.user_names = MultiWebElement(self.browser, self.USER_NAMES_LOC,
                                          description="Hovers Page -> User Names")

    def get_n_user_name(self, index):
        user_cont = self.user_containers[index]
        name = self.user_names[index]

        ActionChains(self.browser.driver) \
            .move_to_element(user_cont.wait_for_visible()) \
            .perform()

        return name.get_text()
