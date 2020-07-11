from skillsearch import prepare_chrome_driver, get_pracuj_main_page, \
    extract_categories
from utils.config import Config


def run():
    pracuj_address = Config.pracuj_address
    page_search_limit = Config.page_search_limit
    driver_path = Config.chrome_driver_path

    driver = prepare_chrome_driver(driver_path)
    get_pracuj_main_page(pracuj_address, driver)
    extract_categories()

if __name__ == '__main__':
    run()
