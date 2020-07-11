from skillsearch import prepare_chrome_driver, get_website, \
    get_job_urls
from utils.config import Config


def run():
    pracuj_address = Config.pracuj_address
    page_search_limit = Config.page_search_limit
    driver_path = Config.chrome_driver_path
    # todo: fetch it from website automatically
    # todo: check if there are IT job offers in other categories than these
    pracuj_it_links = ["https://www.pracuj.pl/praca/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016",
                       "https://www.pracuj.pl/praca/it%20-%20administracja;cc,5015"]

    driver = prepare_chrome_driver(driver_path)
    it_rozwoj_opr = get_website(pracuj_it_links[0], driver)
    job_urls = get_job_urls(it_rozwoj_opr)
    print(job_urls)


if __name__ == '__main__':
    run()
