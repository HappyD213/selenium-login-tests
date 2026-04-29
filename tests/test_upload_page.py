from pages.upload_img_page import UploadImgPage
from config.config_reader import ConfigReader


def test_upload_page(browser):
    browser.get(ConfigReader.get_upload_page_url())
    upload_img_page = UploadImgPage(browser)
    upload_img_page.wait_for_open()

    filepath = r"C:\Users\happyden\Pictures\Screenshots\anvil.png"
    upload_img_page.select_button_send_filepath(filepath)
    upload_img_page.submit_button_click()

    expected_file_name = "anvil.png"
    actual_file_name = upload_img_page.get_upload_file_name()
    assert expected_file_name in actual_file_name, f"Actual: {actual_file_name} != Expected: {expected_file_name}"
