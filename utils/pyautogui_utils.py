import time
import platform
from logger.logger import Logger

if platform.system() == "Windows":
    import pyautogui


class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Handle File Dialog for uploading file")
        time.sleep(3)  # timeout after opening File Dialog

        Logger.debug(f"Write '{file_path}' to search File Dialog field")
        pyautogui.typewrite(file_path)
        Logger.debug("Press enter")
        pyautogui.hotkey("enter")

        time.sleep(3)  # timeout before closing File Dialog
