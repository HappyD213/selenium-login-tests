from elements.input import Input
from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.label import Label
from elements.button import Button
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser


class UploadImgPage(BasePage):
    UNIQUE_ELEMENT_LOC = "drag-drop-upload"
    FILE_UPLOAD_FIELD_LOC = "drag-drop-upload"
    SELECT_FILE_BUTTON_LOC = "file-upload"
    SUBMIT_FILE_BUTTON_LOC = "file-submit"
    UPLOAD_FILE_NAME_LOC = "uploaded-files"
    UPLOAD_FILE_NAME_FROM_FIELD_LOC = "//span[@data-dz-name and normalize-space(.)!='']"
    CHECK_MARK_LOC = "//span[text()='✔']"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Upload Image Page"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Upload Image Page -> = Unique Element")
        self.file_upload_field = WebElement(self.browser, self.FILE_UPLOAD_FIELD_LOC,
                                            description="Upload Image Page -> = File Upload Field Element")
        self.select_file_button = Input(self.browser, self.SELECT_FILE_BUTTON_LOC,
                                        description="Upload Image Page -> = Select File Button Element")
        self.submit_button = Button(self.browser, self.SUBMIT_FILE_BUTTON_LOC,
                                    description="Upload Image Page -> = Submit File Button Element")
        self.upload_file_name = Label(self.browser, self.UPLOAD_FILE_NAME_LOC,
                                      description="Upload Image Page -> = Upload File Name Element")
        self.upload_file_name_from_field = Label(self.browser, self.UPLOAD_FILE_NAME_FROM_FIELD_LOC,
                                                 description="Upload Image Page -> = Upload File Name From Field")
        self.check_mark = Label(self.browser, self.CHECK_MARK_LOC,
                                description="Upload Image Page -> = Check Mark")

    def select_button_send_filepath(self, filepath: str):
        self.select_file_button.send_keys(filepath)

    def submit_button_click(self):
        self.submit_button.click()

    def get_upload_file_name(self) -> str:
        text = self.upload_file_name.get_text()
        return text

    def upload_field_click(self):
        self.file_upload_field.click()

    def get_upload_file_name_from_field(self) -> str:
        text = self.upload_file_name_from_field.get_text()
        return text

    def get_check_mark_from_field(self) -> str:
        check_mark = self.check_mark.get_text()
        return check_mark
