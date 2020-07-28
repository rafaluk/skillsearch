from time import time
from datetime import datetime
import logging


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_time = end_time - start_time
        logging.info(f"Execution of {func.__name__!r} done in {round(elapsed_time, 2)} seconds.")
        return result
    return wrapper


def now():
    return datetime.now().strftime("%c")


def read_skills(filename):
    with open(filename, 'r') as file:
        skills = [line.rstrip('\n') for line in file]
    return skills


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def save_offer_output(filename, offers):
    def concat_offer_parts(offer):
        skills = ','.join(offer.skills)
        return str(offer.position) + '|' + str(offer.url) + '|' + str(skills)

    with open(filename, "w+", encoding='utf-8') as outfile:
        offers = [concat_offer_parts(offer) for offer in offers]
        outfile.write("\n".join(offers))


def save_skills_output(filename, skills):
    with open(filename, "w+", encoding='utf-8') as outfile:
        for key, value in skills.items():
            outfile.write(f"{key},{value}\n")