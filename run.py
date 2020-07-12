from link_extractor import LinkExtractor
from utils.config import Config
from driver import Driver
from utils.utils import calculate_time

# run run()
# this will get the chrome driver from hard disk and prepare it for the job
# then a LinkExtactor will get you links to job offers in model Link(link, position)


@calculate_time
def run():
    driver_path = Config.chrome_driver_path
    pracuj_it_links = Config.pracuj_it_links

    driver = Driver().prepare(driver_path)
    extractor = LinkExtractor(driver)
    job_links = extractor.get_all_links(pracuj_it_links)

    print(len(job_links))
    print(job_links)


if __name__ == '__main__':
    run()
