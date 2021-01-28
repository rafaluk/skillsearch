from extractor import LinkExtractor, OfferExtractor
from skill_aggregator import SkillAggregator
from skill_finder import SkillFinder
from utils.config import Config
from utils.driver import Driver
from utils.utils import calculate_time, read_skills, save_offer_output, save_skills_output
import logging
import argparse

@calculate_time
def run(phases=[1,2,3,4]):

    logging.info(f"Starting ETL. Phases to run: {phases}")

    # PHASE 0: DRIVER - prepare chrome driver
    driver = Driver().prepare(Config.chrome_driver_path)

    # PHASE 1: LINK EXTRACTION - get links to job offers in Link data model
    if 1 in phases:
        job_links = run_link_extraction(driver)

    # PHASE 2: OFFER EXTRACTION - get into all offers and get their content in Offer data model
    if 2 in phases:
        job_offers = run_offer_extraction(driver, job_links)

    # PHASE 3: SKILL FINDING - get skills from offers in OfferWithSkills data model
    if 3 in phases:
        job_offers_with_skills = run_skill_finding(job_offers)

    # PHASE 4: SKILL AGGREGATION - aggregate skills into a dictionary of skills with quantities
    if 4 in phases:
        run_skill_aggregation(job_offers_with_skills)


@calculate_time
def run_link_extraction(driver):
    link_extractor = LinkExtractor(driver=driver)
    job_links = link_extractor.get_all_links(Config.pracuj_it_links)
    logging.info(f"Got {len(job_links)} job links.")
    return job_links


@calculate_time
def run_offer_extraction(driver, job_links):
    offer_extractor = OfferExtractor(driver=driver)
    job_offers = offer_extractor.get_all_offers(job_links)
    logging.info(f"Got {len(job_offers)} job offers.")
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--phases", help="Specify phases to be run, e.g.: 1 or 1-2 or 2-4 (default: all phases).")
    args = vars(parser.parse_args())
    logging.basicConfig(filename='log.log', level=logging.INFO,
                        format='%(asctime)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    if args['phases'] is not None:
        run(phases = args['phases'])
    else: 
        run()
