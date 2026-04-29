from pages.upload_img_page import UploadImgPage
from config.config_reader import ConfigReader
from utils.pyautogui_utils import PyAutoGUIUtilities


def test_upload_img_and_dialog_window(browser):
    browser.get(ConfigReader.get_upload_page_url())
    upload_img_page = UploadImgPage(browser)
    upload_img_page.wait_for_open()

    upload_img_page.upload_field_click()
    filepath = r"C:\Users\happyden\Pictures\Screenshots\anvil.png"
    PyAutoGUIUtilities.upload_file(filepath)
    expected_file_name = "anvil.png"
    actual_file_name = upload_img_page.get_upload_file_name_from_field()
    assert expected_file_name in actual_file_name, f"Expected: {expected_file_name} Actual: {actual_file_name}"

    expected_check_mark = "✔"
    actual_check_mark = upload_img_page.get_check_mark_from_field()
    assert expected_check_mark in actual_check_mark, f"Expected: {expected_check_mark} Actual: {actual_check_mark}"
