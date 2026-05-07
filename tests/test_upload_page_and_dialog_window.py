import pytest
import platform
from pathlib import Path
from config.config import Config
from pages.upload_img_page import UploadImgPage


@pytest.mark.skipif(
    platform.system() != "Windows",
    reason="Requires Windows GUI")
def test_upload_img_and_dialog_window(browser):
    from utils.pyautogui_utils import PyAutoGUIUtilities

    browser.get(Config.UPLOAD_PAGE_URL)
    upload_img_page = UploadImgPage(browser)
    upload_img_page.wait_for_open()

    upload_img_page.upload_field_click()

    file_path = Path("./test_data/test_images/anvil.png").resolve()

    PyAutoGUIUtilities.upload_file(str(file_path))
    expected_file_name = "anvil.png"
    actual_file_name = upload_img_page.get_upload_file_name_from_field()
    assert expected_file_name in actual_file_name, f"Expected: {expected_file_name} Actual: {actual_file_name}"

    expected_check_mark = "✔"
    actual_check_mark = upload_img_page.get_check_mark_from_field()
    assert expected_check_mark in actual_check_mark, f"Expected: {expected_check_mark} Actual: {actual_check_mark}"
