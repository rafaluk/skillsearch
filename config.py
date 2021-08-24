from dataclasses import dataclass


@dataclass
class Config:
    page_search_limit: int = 50
    chrome_driver_path: str = "C:/Users/rklat001/chromedriver/chromedriver.exe"

    pracuj_it_links: tuple = (
        "https://www.pracuj.pl/praca/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016"
        , "https://www.pracuj.pl/praca/it%20-%20administracja;cc,5015"
    )
    
    reed_links: tuple = (
        "https://www.reed.co.uk/jobs/work-from-home-developer-jobs?contract=True",
        # "https://www.reed.co.uk/jobs/work-from-home-data-science-jobs?contract=True",
        # "https://www.reed.co.uk/jobs/work-from-home-data-scientist-jobs?contract=True",
        # "https://www.reed.co.uk/jobs/work-from-home-python-jobs?contract=True"
    )
