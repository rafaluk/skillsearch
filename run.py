from extractor import LinkExtractor, OfferExtractor
from skill_aggregator import SkillAggregator
from skill_finder import SkillFinder
from utils.config import Config
from utils.driver import Driver
from utils.utils import calculate_time, read_skills, save_offer_output, save_skills_output


@calculate_time
def run():
    """This will:
        * prepare the driver for web scraping
        * get links to all job offers from all pages in specified categories
        * get content of every job offer
        * search for specified technologies within all offers
        """
    # prepare chrome driver
    driver = Driver().prepare(Config.chrome_driver_path)

    # get job offers in Link data model
    link_extractor = LinkExtractor(driver=driver)
    job_links = link_extractor.get_all_links(Config.pracuj_it_links)

    print(f"Got {len(job_links)} job links.")

    # get into an offer and get it's content in Offer data model
    offer_extractor = OfferExtractor(driver=driver)
    job_offers = offer_extractor.get_all_offers(job_links)

    print(f"Got {len(job_offers)} job offers.")

    # get skills from offers in OfferWithSkills data model
    skill_extractor = SkillFinder(skills=read_skills("skills.txt"))
    job_offers_with_skills = skill_extractor.get_skills_for_all(job_offers)

    # save output to file
    save_offer_output(filename="outputs/offers_with_skills.csv", offers=job_offers_with_skills)

    skill_aggregator = SkillAggregator()
    skills = skill_aggregator.process_all_offers(job_offers_with_skills)

    # save output to file
    save_skills_output(filename="outputs/skills_with_quantities.csv", skills=skills)


if __name__ == '__main__':
    run()
