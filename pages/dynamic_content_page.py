from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Dynamic Content')]"
    IMAGE_LOC = "(//img[contains(@src, 'avatar')])[{}]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Dynamic Content Page"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Dynamic Content Page -> Unique Element")
        self.images = MultiWebElement(self.browser, self.IMAGE_LOC,
                                      description="Dynamic Content Page -> Images Elements")

    def is_duplicate_image(self) -> bool:
        srcs = [image.get_attribute("src") for image in self.images]
        has_duplicates = len(srcs) != len(set(srcs))
        return has_duplicates
