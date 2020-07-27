from link_extractor import LinkExtractor
from offer_extractor import OfferExtractor
from utils.config import Config
from utils.driver import Driver
from utils.utils import calculate_time

# run run()
# this will get the chrome driver from hard disk and prepare it for the job
# then a LinkExtractor will get you links to job offers in model Link(link, position)


@calculate_time
def run():
    # prepare chrome driver
    driver = Driver().prepare(Config.chrome_driver_path)

    # get job offers in Link data model
    link_extractor = LinkExtractor(driver)
    # tu jest zle, bo bierze tyle samo strno z kazdej kategorii
    job_links = link_extractor.get_all_links(Config.pracuj_it_links, 2)

    print(f"Got {len(job_links)} job links.")

    # get into an offer and get it's content in Offer data model
    offer_extractor = OfferExtractor(driver)
    job_offers = offer_extractor.get_all_offers(job_links)

    print(f"Got {len(job_offers)} job offers.")


    print(len(job_offers))
    print('JOB OFFER 1 ------------------------')
    print(job_offers[0].content)
    print('JOB OFFER 2 ------------------------')
    print(job_offers[1].content)


if __name__ == '__main__':
    run()
