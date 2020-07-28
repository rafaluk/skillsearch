from dataclasses import dataclass


@dataclass
class Config:
    pracuj_address = "https://www.pracuj.pl"
    page_search_limit = 14
    chrome_driver_path = "C:/Users/rafal.klat/chromedriver.exe"
    # todo: fetch it from website automatically
    pracuj_it_links = ["https://www.pracuj.pl/praca/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016"
        # ,"https://www.pracuj.pl/praca/it%20-%20administracja;cc,5015"
                       ]