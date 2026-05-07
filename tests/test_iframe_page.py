from pages.iframe_page import IFramePage
from pages.frames_page import FramesPage
from pages.nested_frames_page import NestedPage
from config.config import Config


def test_iframe_page(browser):
    browser.get(Config.IFRAME_URL)
    iframe_page = IFramePage(browser)
    iframe_page.wait_for_open()

    iframe_page.click_nested_frames_btn()

    nested_frames_page = NestedPage(browser)
    nested_frames_page.wait_for_open()

    expected_parent_frame_text = "Parent frame"
    actual_parent_frame_text = nested_frames_page.get_parent_frame_text()

    assert expected_parent_frame_text in actual_parent_frame_text, (f"Expected: {expected_parent_frame_text} != "
                                                                    f"Actual: {actual_parent_frame_text}")

    expected_child_frame_text = "Child Iframe"
    actual_child_frame_text = nested_frames_page.get_child_frame_text()

    assert expected_child_frame_text in actual_child_frame_text, (f"Expected: {expected_child_frame_text} != "
                                                                  f"Actual: {actual_child_frame_text}")

    iframe_page.click_frames_page_btn()

    frames_page = FramesPage(browser)
    frames_page.wait_for_open()

    first_frame_text = frames_page.get_first_frame_text()
    second_frame_text = frames_page.get_second_frame_text()

    assert first_frame_text == second_frame_text, f"Expected: {first_frame_text} != {second_frame_text}"
