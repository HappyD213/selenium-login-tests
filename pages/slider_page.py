from typing import TYPE_CHECKING

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

if TYPE_CHECKING:
    from browser.browser import Browser


class SliderPage(BasePage):
    SLIDER_LOC = '//div[contains(@class,"sliderContainer")]//input[@type="range"]'
    CURRENT_RANGE_LOC = 'range'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.name = 'SliderPage'

        self.unique_element = WebElement(self.browser, self.SLIDER_LOC, description=f"Slider Page -> Unique Element")
        self.result_element = Label(self.browser, self.CURRENT_RANGE_LOC, description=f"Slider Page -> Result Element")

    def set_slider_value(self, value_to_set: int) -> None:
        max_value = float(self.unique_element.get_attribute("max"))
        min_value = float(self.unique_element.get_attribute("min"))
        slider = self.unique_element.wait_for_clickable()

        if value_to_set > max_value or value_to_set < min_value:
            raise ValueError(f"Slider value must be between {min_value} and {max_value} your value is {value_to_set}")

        self.browser.execute_script("""
                                    arguments[0].value = arguments[1];
                                    arguments[0].dispatchEvent(new Event('input'));
                                    arguments[0].dispatchEvent(new Event('change'));
                                    """,
                                    slider,
                                    value_to_set)

    def get_result_text(self) -> str:
        text = self.result_element.get_text()
        return text
