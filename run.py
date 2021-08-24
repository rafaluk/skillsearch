from extractor import LinkExtractor, OfferExtractor
from skill_aggregator import SkillAggregator
from skill_finder import SkillFinder
from config import Config
from utils import driver, utils
import logging
import argparse
from datetime import datetime

@utils.calculate_time
def run(timestamp, phases=[1,2,3,4]):

    logging.info(f"Starting ETL. Phases to run: {phases}")

    # PHASE 0: DRIVER - prepare chrome driver
    d = driver.Driver().prepare(Config.chrome_driver_path)

    # PHASE 1: LINK EXTRACTION - get links to job offers and save them in Link data model
    if 1 in phases:
        job_links = run_link_extraction(d, timestamp)

    # PHASE 2: OFFER EXTRACTION - extract content from offers from all links and save their content in Offer data model
    if 2 in phases:
        job_offers = run_offer_extraction(d, job_links, timestamp)

    # PHASE 3: SKILL FINDING - get skills from offers in OfferWithSkills data model
    if 3 in phases:
        job_offers_with_skills = run_skill_finding(job_offers, timestamp, "developer_keywords.txt")

    # PHASE 4: SKILL AGGREGATION - aggregate skills into a dictionary of skills with quantities
    if 4 in phases:
        run_skill_aggregation(job_offers_with_skills, timestamp)


@utils.calculate_time
def run_link_extraction(driver, timestamp):
    
    # Initiate LinkExtractor
    link_extractor = LinkExtractor(driver=driver)
    logging.info(f"Link extraction started.")
    
    # Run LinkExtractor
    job_links = link_extractor.get_all_links(Config.reed_links)
        
    logging.info(f"Got {len(job_links)} job links.")
    logging.info("Links extraction finished.")
    
    # Save output to .csv file
    filename = "outputs/extracted_links" + timestamp
    utils.save_links(filename=filename, links=job_links)
    logging.info("Links extracted and saved to file.")
    
    return job_links


@utils.calculate_time
def run_offer_extraction(driver, job_links, timestamp):
    
    # Initiate OfferExtractor
    offer_extractor = OfferExtractor(driver=driver)
    logging.info("Offer extraction started.")

    # Run OfferExtractor
    job_offers = offer_extractor.get_all_offers(job_links)
    logging.info("Offer extraction finished.")
    
    # TODO: Saving offers. There's no point in saving huge HTMLs to .csv.
    # Save output to .csv file
    ## filename = "outputs/extracted_offers" + timestamp + ".csv"

    return job_offers


@utils.calculate_time
def run_skill_finding(job_offers, timestamp, keywords):
    
    # Initiate SkillFinder
    skill_finder = SkillFinder(skills=utils.read_skills(keywords))
    logging.info("Skill finding started.")
    
    # Run SkillFinder
    job_offers_with_skills = skill_finder.get_skills_for_all(job_offers)
    logging.info("Skill finding finished.")
    
    # Save output to .csv file
    filename = "outputs/offers_with_skills" + timestamp + ".csv"
    utils.save_offer_output(filename=filename, offers=job_offers_with_skills)
    
    return job_offers_with_skills


@utils.calculate_time
def run_skill_aggregation(job_offers_with_skills, timestamp):
    
    # Initiate SkillAggregator
    skill_aggregator = SkillAggregator()
    logging.info("Skill aggregation started.")
    
    # Run SkillAggregator
    skills = skill_aggregator.process_all_offers(job_offers_with_skills)
    logging.info("Skill aggregation finished.")

    # Save output to file
    filename = "outputs/skills_with_quantities" + timestamp + ".csv"
    utils.save_skills_output(filename=filename, skills=skills)
    
    return skills


if __name__ == '__main__':
    
    # Create current run timestamp
    current_run_timestamp = datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')
    
    # Read stdin arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--phases", help="Specify phases to be run, e.g.: 1 or 1-2 or 2-4 (default: all phases).")
    args = vars(parser.parse_args())
    
    # Configure logging (logs go to file and to stdout)
    log_filename = 'logs/run' + current_run_timestamp + '.log'
    logging.basicConfig(filename=log_filename, level=logging.INFO,
                        format='%(asctime)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    logging.getLogger().addHandler(logging.StreamHandler())
    
    # Run ETL with specified phases
    if args['phases'] is not None:
        phases = utils.parse_phases(args['phases'])
        run(timestamp=current_run_timestamp, phases=phases)
    else: 
        run(timestamp=current_run_timestamp)
