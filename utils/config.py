from dataclasses import dataclass


@dataclass
class Config:
    page_search_limit: int = 6
    chrome_driver_path: str = "C:/Users/rafal.klat/chromedriver.exe"
    # todo: fetch it from website automatically
    pracuj_it_links: list = (
        "https://www.pracuj.pl/praca/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016"
        , "https://www.pracuj.pl/praca/it%20-%20administracja;cc,5015"
    )
