import time
import pytest

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DocumentReady:
    def __call__(self, driver):
        try:
            return driver.execute_script("return document.readyState") == "complete"
        except:
            return False

class ElementHasText:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element = driver.find_element(*self.locator)
            text = element.text.strip()
            return text if text else False
        except:
            return False

class Locators:
    MAIN_PAGE_UNIQUE = (By.XPATH, "//h2[@id='home_featured_and_recommended']")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class,'global_action_link') and contains(@href, 'login')]")

    LOGIN_PAGE_UNIQUE = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]")
    LOGIN_INPUT_TEXT = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]//input[@type='text']")
    LOGIN_INPUT_PASSWORD = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]//button[@type='submit']")
    LOADING_BUTTON_ELEMENT = (By.XPATH, "//button[@type='submit']/div/div")
    ERROR_TEXT_ELEMENT = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]//form/div[last()]")

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_with_invalid_credentials_shows_error(browser):
    timeout = 10
    url = "https://store.steampowered.com/"
    wait = WebDriverWait(browser, timeout)
    fake = Faker()

    #Navigate to main page
    browser.get(url)
    wait.until(DocumentReady())
    wait.until(EC.visibility_of_element_located(Locators.MAIN_PAGE_UNIQUE))
    #Click login button
    wait.until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).click()
    wait.until(DocumentReady())
    wait.until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_UNIQUE))
    #Input random strings as credentials. Click sign in button
    wait.until(EC.visibility_of_element_located(Locators.LOGIN_INPUT_TEXT)).send_keys(fake.text(8))
    wait.until(EC.visibility_of_element_located(Locators.LOGIN_INPUT_PASSWORD)).send_keys(fake.text(8))
    wait.until(EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(Locators.LOADING_BUTTON_ELEMENT))
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))

    actual_text = wait.until(ElementHasText(Locators.ERROR_TEXT_ELEMENT))
    expected_text = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
    assert expected_text in actual_text, f"Expected text not found in actual text: {actual_text}"
