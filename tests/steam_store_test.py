import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage

@pytest.mark.parametrize(
    "game_name, n",
    [
        ("The witcher", 10),
        ("Fallout", 20),
    ]
)
def  test_search_games(browser, game_name, n):
    main_page = MainPage(browser)

    main_page.open_main_page()
    search_page = main_page.search_game(game_name)
    search_page.search_page_is_displayed()
    search_page.sort_price_by_desc()
    search_page.get_games_list(n)

