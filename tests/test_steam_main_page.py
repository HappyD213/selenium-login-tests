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

class LOCATORS:
    MAIN_PAGE_UNIQUE = (By.XPATH, "//div[contains(@class,'home_cluster_ctn') and contains(@class,'home_ctn')]")
    MAIN_PAGE_UNIQUE2 = (By.XPATH, "//h2[@id='home_featured_and_recommended']")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class,'global_action_link') and contains(@href, 'login')]")

    LOGIN_PAGE_UNIQUE = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]")
    LOGIN_INPUT_TEXT = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]//input[@type='text']")
    LOGIN_INPUT_PASSWORD = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]//button[@type='submit']")
    LOADING_BUTTON_ELEMENT = (By.XPATH, "//button[@type='submit']/div/div")
    ERROR_TEXT = (By.XPATH, "//div[contains(@class,'login_featuretarget_ctn')]//form/div[last()]")

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_with_invalid_credentials_shows_error(browser):
    URL = "https://store.steampowered.com/"
    WAIT = WebDriverWait(browser, 10)
    fake = Faker()

    #Navigate to main page
    browser.get(URL)
    WAIT.until(DocumentReady())
    WAIT.until(EC.visibility_of_element_located(LOCATORS.MAIN_PAGE_UNIQUE))
    WAIT.until(EC.visibility_of_element_located(LOCATORS.MAIN_PAGE_UNIQUE2))
    #Click login button
    WAIT.until(EC.visibility_of_element_located(LOCATORS.LOGIN_BUTTON)).click()
    WAIT.until(DocumentReady())
    WAIT.until(EC.visibility_of_element_located(LOCATORS.LOGIN_PAGE_UNIQUE))
    #Input random strings as credentials. Click sign in button
    WAIT.until(EC.visibility_of_element_located(LOCATORS.LOGIN_INPUT_TEXT)).send_keys(fake.text(8))
    WAIT.until(EC.visibility_of_element_located(LOCATORS.LOGIN_INPUT_PASSWORD)).send_keys(fake.text(8))
    WAIT.until(EC.visibility_of_element_located(LOCATORS.LOGIN_SUBMIT_BUTTON)).click()
    WAIT.until(EC.visibility_of_element_located(LOCATORS.LOADING_BUTTON_ELEMENT))
    WAIT.until(EC.visibility_of_element_located(LOCATORS.ERROR_TEXT))