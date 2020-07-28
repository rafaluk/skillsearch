from extractor import LinkExtractor, OfferExtractor
from skill_aggregator import SkillAggregator
from skill_finder import SkillFinder
from utils.config import Config
from utils.driver import Driver
from utils.utils import calculate_time, read_skills, save_offer_output, save_skills_output


@calculate_time
def run():
    """This will run all phases"""

    # PHASE: DRIVER - prepare chrome driver
    driver = Driver().prepare(Config.chrome_driver_path)

    # PHASE: LINK EXTRACTION - get job offers in Link data model
    job_links = run_link_extraction(driver)

    # PHASE: OFFER EXTRACTION - get into an offer and get it's content in Offer data model
    job_offers = run_offer_extraction(driver, job_links)

    # PHASE: SKILL FINDING - get skills from offers in OfferWithSkills data model
    job_offers_with_skills = run_skill_finding(job_offers)

    # PHASE: SKILL AGGREGATION - aggregate skills into a dictionary of skills with quantities
    run_skill_aggregation(job_offers_with_skills)


@calculate_time
def run_link_extraction(driver):
    link_extractor = LinkExtractor(driver=driver)
    job_links = link_extractor.get_all_links(Config.pracuj_it_links)
    print(f"Got {len(job_links)} job links.")
    return job_links


@calculate_time
def run_offer_extraction(driver, job_links):
    offer_extractor = OfferExtractor(driver=driver)
    job_offers = offer_extractor.get_all_offers(job_links)
    print(f"Got {len(job_offers)} job offers.")
    return job_offers


@calculate_time
def run_skill_finding(job_offers):
    skill_finder = SkillFinder(skills=read_skills("skills.txt"))
    job_offers_with_skills = skill_finder.get_skills_for_all(job_offers)
    # save output to file
    save_offer_output(filename="outputs/offers_with_skills.csv", offers=job_offers_with_skills)
    return job_offers_with_skills


@calculate_time
def run_skill_aggregation(job_offers_with_skills):
    skill_aggregator = SkillAggregator()
    skills = skill_aggregator.process_all_offers(job_offers_with_skills)
    # save output to file
    save_skills_output(filename="outputs/skills_with_quantities.csv", skills=skills)


if __name__ == '__main__':
    run()
