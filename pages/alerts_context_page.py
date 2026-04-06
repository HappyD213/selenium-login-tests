from browser.browser import Browser
from logger.logger import Logger
from pages.base_page import BasePage
from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from selenium.webdriver.common.action_chains import ActionChains


class AlertContextPage(BasePage):
    ALERT_CONTEXT_UNIQUE = "hot-spot"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.name = 'Alert Context Page'

        self.unique_element = WebElement(self.browser, self.ALERT_CONTEXT_UNIQUE, description="Alerts Context Page -> Unique element")


    def context_click(self):
        Logger.info(f"{self}: context_click")
        ActionChains(self.browser.driver) \
            .context_click(self.unique_element.wait_for_clickable()) \
            .perform()