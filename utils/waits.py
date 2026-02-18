from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def document_ready():
    def wait_func(driver):
        return driver.execute_script("return document.readyState == 'complete'")

    return wait_func


def element_has_text(locator):
    def wait_func(driver):
        try:
            element = driver.find_element(*locator)
            text = element.text.strip()
            return text if text else False

        except:
            return False

    return wait_func
