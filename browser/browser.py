import time
from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from elements.base_element import BaseElement
from logger.logger import Logger


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 120
    FAST_FREQUENCY = 0.1

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.set_page_load_timeout(Browser.DEFAULT_TIMEOUT)

        self.main_handle = None
        self._wait = WebDriverWait(self._driver, timeout=self.DEFAULT_TIMEOUT)
        self._fast_wait = WebDriverWait(self._driver, timeout=self.DEFAULT_TIMEOUT, poll_frequency=self.FAST_FREQUENCY)

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def get(self, url: str) -> None:
        Logger.info(f"{self}: get '{url}'")
        try:
            self._driver.get(url)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        self.main_handle = self._driver.current_window_handle

    def close(self) -> None:
        Logger.info(f"{self}: close window handle '{self._driver.current_window_handle}'")
        self._driver.close()

    def back(self) -> None:
        Logger.info(f"{self}: performing driver.back()")
        self._driver.back()

    def quit(self) -> None:
        Logger.info(f"{self}: quit")
        try:
            self._driver.quit()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def execute_script(self, script: str, *args) -> None:
        Logger.info(f"{self}: execute script = '{script}' with args = '{args}'")
        try:
            self._driver.execute_script(script, *args)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def save_screenshot(self, filename: str) -> None:
        Logger.info(f"{self}: save screenshot in '{filename}'")
        self._driver.save_screenshot(filename=filename)

    def switch_to_default_window(self) -> None:
        Logger.info(f"{self}: switch to default browser")
        try:
            self._driver.switch_to.window(self.main_handle)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def switch_to_window(self, title: str) -> None:
        Logger.info(f"{self}: switch to window with title '{title}'")
        end_time = time.time() + self.PAGE_LOAD_TIMEOUT
        while True:
            handles = self._driver.window_handles
            for handle in handles:
                self._driver.switch_to.window(handle)
                if self._driver.title == title:
                    Logger.info(f"{self}: new window handle = '{self._driver.current_window_handle}'")
                    return
            if time.time() < end_time:
                time.sleep(1)
            else:
                Logger.error(f"{self}: windows with title '{title}' wasn't found")
                raise ValueError(f"{self}: windows with title '{title}' wasn't found")

    def wait_alert_present(self):
        Logger.info(f"{self}: wait alert present")
        return self._wait.until(EC.alert_is_present())

    def wait_alert_gone(self):
        Logger.info(f"{self}: wait alert gone")
        return self._wait.until_not(EC.alert_is_present())

    def get_alert_text(self):
        Logger.info(f"{self}: get alert text")
        return self.wait_alert_present().text

    def accept_alert(self):
        Logger.info(f"{self}: accept alert")
        self.wait_alert_present().accept()

    def send_keys_alert(self, text: str):
        Logger.info(f"{self}: send '{text}' to alert'")
        self.wait_alert_present().send_keys(text)

    def switch_to_frame(self, frame: BaseElement):
        Logger.info(f"{self}: switch to frame")
        return self._driver.switch_to.frame(frame.wait_for_presence())

    def switch_to_default_content(self):
        Logger.info(f"{self}: switch to default content")
        self._driver.switch_to.default_content()

    def get_current_window_handles(self):
        Logger.info(f"{self}: get current window handles")
        return self._driver.window_handles

    def wait_new_page_opened(self, current_handles: set[str]):
        Logger.info(f"{self}: wait new page opened")
        old_handles = set(current_handles)
        return self._wait.until(EC.new_window_is_opened(old_handles))

    def new_window_to_be_available_and_switch_to_it(self, current_handles: set[str]):
        Logger.info(f"{self}: wait new window is opened and switch to it")
        old_handles = set(current_handles)
        self.wait_new_page_opened(old_handles)
        actual_handles = set(self._driver.window_handles)
        new_window_handle = (actual_handles - old_handles).pop()
        self._driver.switch_to.window(new_window_handle)

    def get_current_title(self):
        Logger.info(f"{self}: get current title")
        return self._driver.title

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self._driver.session_id}]"

    def __repr__(self) -> str:
        return str(self)
