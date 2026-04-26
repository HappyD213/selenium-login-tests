from random import choice
from typing import TYPE_CHECKING
from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from selenium.webdriver.common.keys import Keys

if TYPE_CHECKING:
    from browser.browser import Browser


class SliderPage(BasePage):
    SLIDER_LOC = '//div[contains(@class,"sliderContainer")]//input[@type="range"]'
    CURRENT_RANGE_LOC = 'range'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'SliderPage'

        self.unique_element = WebElement(self.browser, self.SLIDER_LOC, description=f"Slider Page -> Unique Element")
        self.slider_element = Input(self.browser, self.SLIDER_LOC, description=f"Slider Page -> Slider Element")
        self.result_element = Label(self.browser, self.CURRENT_RANGE_LOC, description=f"Slider Page -> Result Element")

    def set_slider_value(self, value_to_set: float) -> None:
        self.slider_element.click()
        step_value = float(self.unique_element.get_attribute("step"))
        current_value = float(self.unique_element.get_attribute("value"))
        steps = round((value_to_set - current_value) / step_value)

        if steps < 0:
            self.slider_element.send_keys(Keys.ARROW_LEFT * abs(steps))
        elif steps > 0:
            self.slider_element.send_keys(Keys.ARROW_RIGHT * steps)

    def get_random_value_for_slider(self) -> float:
        step = float(self.slider_element.get_attribute("step"))
        min_value = float(self.slider_element.get_attribute("min"))
        max_value = float(self.slider_element.get_attribute("max"))

        possible_values = []
        current_value = min_value

        while current_value <= max_value:
            possible_values.append(current_value)
            current_value += step

        return choice(possible_values)

    def get_result_text(self) -> str:
        text = self.result_element.get_text()
        return text
