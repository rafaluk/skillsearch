from bs4 import BeautifulSoup
from data_model import Link
from config import Config
from utils.utils import calculate_time, is_int
from data_model import Offer
import logging
from typing import List


class Extractor:
    def __init__(self, driver):
        self.driver = driver

    @calculate_time
    def get_website(self, url):
        print(f'get_website {url=}')
        self.driver.get(url)
        logging.info(f"Got website: {url}")
        return self.driver.page_source

    @staticmethod
    def transform_to_bs4(page_source):
        return BeautifulSoup(page_source, features="html.parser")


class LinkExtractor(Extractor):
    def __init__(self, driver):
        Extractor.__init__(self, driver)
        self.links = []

    def get_jobs(self, page_source):
        page_bs4 = self.transform_to_bs4(page_source)
        titles = page_bs4.find_all("h3", class_="title")
        offers = [x.find("a") for x in titles]
        return [Link('https://www.reed.co.uk' + offer['href'], offer.getText()) for offer in offers]

    @calculate_time
    def get_all_links(self, category_links):
        max_no_of_pages = Config.page_search_limit
        
        for category_link in category_links:
            
            # limiting number of pages, if there are too many of them
            # no_of_pages = min(self.get_no_of_pages(category_link), max_no_of_pages)
            # logging.info(f'Searching {no_of_pages} pages in category: {category_link}')
            
            # for site_no in range(1, 2):
            for site_no in range(1, max_no_of_pages):

                address_to_get = category_link + "&pageno=" + str(site_no)
                source = self.get_website(address_to_get)
                self.links += self.get_jobs(source)
        return self.links

    @calculate_time
    def get_no_of_pages(self, category_link):
        try:
            page_source = self.get_website(category_link)
            page_bs4 = self.transform_to_bs4(page_source)
            number_containers = page_bs4.find_all("a", class_="pagination_trigger")
            numbers = [int(cont.get_text()) if is_int(cont.get_text()) else 0 for cont in number_containers]
            return max(numbers)
        except:
            logging.error("Not able to get number of pages.")
            return 1000


class OfferExtractor(Extractor):
    def __init__(self, driver):
        Extractor.__init__(self, driver)
        self.offers = []

    def get_offer(self, page_source, url, position):
        page_bs4 = self.transform_to_bs4(page_source)
        offer_container = page_bs4.find("div", {"class": "description-container row"})

        return Offer(url, position, str(offer_container))

    @calculate_time
    def get_all_offers(self, links):
        for link in links:
            page_source = self.get_website(link.url)
            offer = self.get_offer(page_source, link.url, link.position)
            self.offers.append(offer)
        return self.offers
