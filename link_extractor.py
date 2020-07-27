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


class SkillExtractor:
    def __init__(self, links, driver):
        self.links: Link = links
        self.driver = driver

    def get_page_source(self, url):
        pass

    def get_offer_details(self, page_source):
        pass

    def get_skills(self, offer_details):
        pass

# this is unnecessary, since I hardcoded links to IT categories
# @calculate_time
# def extract_categories(pracuj_main_page, allowed_categories):
#     pracuj_main_page_bs4 = BeautifulSoup(pracuj_main_page, features="html.parser")
#     pracuj_area_with_links = pracuj_main_page_bs4.find_all("div", class_="grid__seo-box")
#     print(str(pracuj_area_with_links))
#     pattern_json = regex.compile(r'\{(?:[^{}]|(?R))*\}')
#     # print(pracuj_area_with_links)
#     json_string_with_links = pattern_json.findall(str(pracuj_area_with_links))[0]
#     json_links = json.loads(json_string_with_links)['seo']
#     popular_categories = json_links["popularCategories"]
#     print("Popular categories:")
#     print([i['name'] for i in popular_categories])
#
#
#
#     print(f"Allowing these categories only:\n{allowed_categories}")
#
#     # check if all allowed categories are present in popular categories
#     for category in allowed_categories:
#         if category not in popular_categories:
#             print(f"Warning: allowed category {category} is not popular.")
#
#
#     for category in allowed_categories:
#         # tu wchodze w kazdy link, ktory juz mam w jsonie i pobieram linki do ofert pracy
#         pass







# odtad zrobilem comment

# print(f"All category links collected:\n{pracuj_category_links}")
#
# no_of_categories = len(pracuj_category_links)
# print(f"There are {no_of_categories}.")
# category_counter = 0
#
#
# offer_links = []
# # lecimy po kazdej kategorii
# # TODO: ta liczba 15 to tylko dla testow
# for category_link in pracuj_category_links:
#
#     category_counter = 0
#     # pobieramy strone dla kazdej kategorii
#     driver.get(pracuj_address + category_link)
#     category_html = driver.page_source.encode("utf-8")
#     category_html = BeautifulSoup(category_html, features="html.parser")
#     category_name = category_html.find("title").string[6:-12]
#     print(category_name)
#
#     print("\nCategory:", category_name)
#     all_as = category_html.find_all("a", class_="offer-details__title-link")
#
#     # sprawdzmy ile stron jest w kategorii
#     last_category_page = category_html.find_all("a", class_="pagination_trigger")[-2].string
#     last_category_page = int(last_category_page)
#     print("(category pages: " + str(last_category_page) + ")")
#
#     # lecimy po kolejnych stronach
#     # range powinein byc last_category_page, ale wtedy jest za duzo
#     for page_number in range(1, min(PAGE_SEARCH_LIMIT, last_category_page)):
#     # for page_number in range(1, 2):
#
#         # pobieramy strone dla kazdej kategorii, ale zaczynamy od 2
#         driver.get(pracuj_address + category_link + "?pn=" + str(page_number))
#         category_html = driver.page_source.encode("utf-8")
#         category_html = BeautifulSoup(category_html, features="html.parser")
#
#         all_as = category_html.find_all("a", class_="offer-details__title-link")
#
#         # pobieramy linki do wszystkich ofert na stronie
#         ile_na_stronie = 0
#         for a in all_as:
#             ile_na_stronie += 1
#             category_counter += 1
#             link = a.get("href")
#             offer_links.append(link)
#         print(ile_na_stronie, "offers found on page no.",
#               page_number)
#
#     print(category_counter, "offers found in this category.")
#     print(len(offer_links), "offers found in total.")
#     print_time(whole_script_START_TIME, time.time())
#     # usunac po testach
#
#
# # w tym momencie mam linki do wszystkich ofert na pracuj.pl
# # todo co jesli link nie bedzie dzialac, bo oferta expired?
#
# global_list = []
# licznik = 0
#
# # lecimy po kategoriach
# for link in offer_links:
#     licznik+=1
#     # if licznik > 5:
#     #     break
#     link = pracuj_address + link
#     # print(link)
#     oferta = requests.get(link).text
#     category_name = Obrabiacz(oferta)
#     lists_from_offer = category_name.extract_lists_from_offers()
#     print("Offer",licznik, "from", str(len(offer_links)), "(",
#           round(licznik*100/len(offer_links)), "%)")
#     print_time(whole_script_START_TIME, time.time())
#     for i in lists_from_offer:
#         global_list.append(i)
# driver.quit()
#
# all_offers = pd.DataFrame(data=global_list)
# all_offers.to_csv("offers.csv", index=False, header=None, encoding='utf-8')
#
#
