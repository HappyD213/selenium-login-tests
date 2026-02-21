import random
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from utils.waits import document_ready


class SliderPage(BasePage):
    SLIDER = (By.XPATH, '//div[contains(@class,"sliderContainer")]//input[@type="range"]')
    CURRENT_RANGE = (By.ID, 'range')

    def wait_for_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.SLIDER))
        self.wait.until(document_ready())

    def move_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable(self.SLIDER))
        min_value = float(slider.get_attribute('min'))
        max_value = float(slider.get_attribute('max'))
        step = float(slider.get_attribute('step'))

        random_values = [min_value + i * step for i in range(1, int((max_value - min_value) / step))]
        value = random.choice(random_values)

        slider_width = slider.size['width']

        relative_value = (value - min_value) / (max_value - min_value)
        x_offset = relative_value * slider_width
        x_offset_corrected = x_offset - (slider_width / 2)

        ActionChains(self.driver) \
            .click_and_hold(slider) \
            .move_by_offset(x_offset_corrected, 0) \
            .release() \
            .perform()
        return int(value)

    def get_current_value(self):
        text = self.wait.until(EC.visibility_of_element_located(self.CURRENT_RANGE)).text
        return int(text)
