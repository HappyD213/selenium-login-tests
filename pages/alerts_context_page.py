from browser.browser import Browser
from logger.logger import Logger
from pages.base_page import BasePage
from elements.web_element import WebElement
from selenium.webdriver.common.action_chains import ActionChains


class AlertContextPage(BasePage):
    ALERT_CONTEXT_UNIQUE_LOC = "hot-spot"
    ALERT_CONTEXT_MENU_LOC = "hot-spot"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.name = 'Alert Context Page'

        self.unique_element = WebElement(self.browser, self.ALERT_CONTEXT_UNIQUE_LOC,
                                         description="Alerts Context Page -> Unique element")
        self.alert_context_menu = WebElement(self.browser, self.ALERT_CONTEXT_MENU_LOC,
                                             description="Alerts Context Page -> Context Menu")

    def right_click_context_menu(self):
        Logger.info(f"{self}: context_click")
        ActionChains(self.browser.driver) \
            .context_click(self.alert_context_menu.wait_for_clickable()) \
            .perform()
