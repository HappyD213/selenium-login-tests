from pages.upload_img_page import UploadImgPage
from config.config import Config
from pathlib import Path


def test_upload_page(browser):
    browser.get(Config.UPLOAD_PAGE_URL)
    upload_img_page = UploadImgPage(browser)
    upload_img_page.wait_for_open()

    base_dir = Path(__file__).resolve().parent.parent
    file_path = str(base_dir.joinpath("test_data", "test_images", "anvil.png"))
    upload_img_page.select_button_send_filepath(file_path)
    upload_img_page.submit_button_click()

    expected_file_name = "anvil.png"
    actual_file_name = upload_img_page.get_upload_file_name()
    assert expected_file_name in actual_file_name, f"Actual: {actual_file_name} != Expected: {expected_file_name}"
