from dataclasses import dataclass


@dataclass
class Config:
    pracuj_address = "https://www.pracuj.pl"
    page_search_limit = 14
    chrome_driver_path = "C:/Users/rafal.klat/chromedriver.exe"
    allowed_categories = {"Inżynieria", "Administracja biurowa",
                          "Marketing", "IT - Rozwój oprogramowania",
                          "IT - Administracja", "Bankowość"}
