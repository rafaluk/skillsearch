from link_extractor import LinkExtractor
from utils.config import Config
from driver import Driver


def run():
    driver_path = Config.chrome_driver_path
    # todo: fetch it from website automatically
    # todo: check if there are IT job offers in other categories than these
    pracuj_it_links = ["https://www.pracuj.pl/praca/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016",
                       "https://www.pracuj.pl/praca/it%20-%20administracja;cc,5015"]

    driver = Driver().prepare(driver_path)
    extractor = LinkExtractor(driver)
    # todo: loop over all pages
    it_rozwoj_opr_source = extractor.get_website(pracuj_it_links[0])

    for site_no in range(1, 5):
        extractor.get_job_urls(it_rozwoj_opr_source + "?pn=" + str(site_no))

    links = extractor.links
    print(len(links))
    print(links)


if __name__ == '__main__':
    run()
