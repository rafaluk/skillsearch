from dataclasses import dataclass


@dataclass
class Config:
    pracuj_address = "https://www.pracuj.pl"
    page_search_limit = 14
    chrome_driver_path = "C:/Users/rafal.klat/chromedriver.exe"
    allowed_categories = {"Inżynieria", "Administracja biurowa",
                          "Marketing", "IT - Rozwój oprogramowania",
                          "IT - Administracja", "Bankowość"}
    # todo: fetch it from website automatically
    # todo: check if there are IT job offers in other categories than these
    pracuj_it_links = ["https://www.pracuj.pl/praca/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016"
                       ,"https://www.pracuj.pl/praca/it%20-%20administracja;cc,5015"
                       ]