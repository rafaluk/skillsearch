from bs4 import BeautifulSoup
from data_model import Offer
from utils.utils import calculate_time


class OfferExtractor:
    def __init__(self, driver):
        self.driver = driver
        self.offers = []

    @calculate_time
    def get_website(self, url):
        self.driver.get(url)
        return self.driver.page_source

    @calculate_time
    def get_offer(self, page_source, url, position):
        page_bs4 = BeautifulSoup(page_source, features="html.parser")
        offer_container = page_bs4.find("div", class_="grid__offer-view")

        return Offer(url, position, str(offer_container))

    @calculate_time
    def get_all_offers(self, links):
        for link in links:
            page_source = self.get_website(link.url)
            offer = self.get_offer(page_source, link.url, link.position)
            self.offers.append(offer)
        return self.offers
