import string
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def random_string(length=8):
    return "".join(random.choices(string.ascii_letters, k=length))

def test_steam_main():
    with webdriver.Chrome() as browser:
        url = 'https://store.steampowered.com/'
        browser.get(url)

        wait = WebDriverWait(browser, 10)

        assert "store.steampowered.com" in browser.current_url
        wait.until(EC.title_contains("Steam"))
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.home_cluster_ctn")))

        btn_to_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.global_action_link[href*='/login/']")))
        btn_to_login.click()
        assert "login" in browser.current_url
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.login_featuretarget_ctn")))

        login_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.login_featuretarget_ctn input[type='text']")))
        password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.login_featuretarget_ctn input[type='password']")))

        login_input.send_keys(random_string())
        password_input.send_keys(random_string())

        btn_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.login_featuretarget_ctn button[type='submit']")))
        btn_login.click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit'] div div")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.login_featuretarget_ctn button[type='submit']")))

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Пожалуйста, проверьте свой пароль')]")))
