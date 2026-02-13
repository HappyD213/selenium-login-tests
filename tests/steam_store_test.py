import pytest
from pages.main_page import MainPage
from pages.search_page import SearchPage
from utils.config_reader import ConfigReader

config = ConfigReader()


@pytest.mark.parametrize(
    "browser, game_name, n",
    [
        ("ru","The witcher", 10),
        ("en","The witcher", 10),
        ("ru","Fallout", 20),
        ("en","Fallout", 20),
    ],
    indirect = ["browser"],
)
def test_search_game(browser, game_name, n):
    browser.get(config.get("DEFAULT", "base_url"))

    main_page = MainPage()
    main_page.is_displayed()
    main_page.search_game(game_name)

    search_page = SearchPage()
    search_page.is_displayed()
    search_page.sort_price_by_desc(n)
    prices = search_page.get_prices(n)
    expected_prices = sorted(prices, reverse=True)
    assert prices == expected_prices, (
        f"Prices are not sorted in descending order.\n"
        f"Actual: {prices}\n"
        f"Expected: {expected_prices}"
    )
