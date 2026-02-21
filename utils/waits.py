from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException


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


def is_alert_closed(driver):
    try:
        driver.switch_to.alert
        return False

    except NoAlertPresentException:
        return True


def get_elements(locator):
    def wait_func(driver):
        elements = driver.find_elements(*locator)
        return elements if elements else False

    return wait_func


def get_users_names(locator):
    def wait_func(driver):
        elements = driver.find_elements(*locator)

        for el in elements:
            if el.text.strip():
                return elements

        return False

    return wait_func
