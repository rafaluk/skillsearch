from bs4 import BeautifulSoup
from data_model import Link
from utils.utils import calculate_time


class LinkExtractor:
    def __init__(self, driver):
        self.driver = driver
        self.links = []

    @calculate_time
    def get_website(self, url):
        self.driver.get(url)
        return self.driver.page_source

    @calculate_time
    def get_jobs(self, page_source):
        page_bs4 = BeautifulSoup(page_source, features="html.parser")
        offers = page_bs4.find_all("a", class_="offer-details__title-link")
        return [Link(offer['href'], offer.getText()) for offer in offers]

    @calculate_time
    def get_all_links(self, category_links, no_of_pages):
        for category_link in category_links:
            # todo: fetch automatically no_of_pages in category
            no_of_pages = no_of_pages
            for site_no in range(1, no_of_pages):
                source = self.get_website(category_link + "?pn=" + str(site_no))
                self.links += self.get_jobs(source)
        return self.links
