from time import time
from datetime import datetime
import logging
import re
import pandas as pd
# import h5py


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
    

def save_links(filename, links):
     df_links = pd.DataFrame(links)
     df_links.to_csv(filename + '.csv')


def save_offer_output(filename, offers):
    def concat_offer_parts(offer):
        skills = ','.join(offer.skills)
        return str(offer.position) + '|' + str(offer.url) + '|' + str(offer.salary) + '|' + str(offer.posted_by) + '|' + str(skills)

    with open(filename, "w+", encoding='utf-8') as outfile:
        offers = [concat_offer_parts(offer) for offer in offers]
        outfile.write("\n".join(offers))


def save_skills_output(filename, skills):
    with open(filename, "w+", encoding='utf-8') as outfile:
        for key, value in skills.items():
            outfile.write(f"{key},{value}\n")


def parse_phases(phases):
    LAST_PHASE_NO = 4

    result = []

    interval_pattern = re.compile("^\d\-\d$")
    int_pattern = re.compile("^\d$")

    def check_limits(number):
        return 1 <= number <= LAST_PHASE_NO

    valueErrorMsg = f'Incorrect phase. Please enter e.g.: 1 or 1-2 or 2-4 (default: all phases). Last phase: {LAST_PHASE_NO}'

    if int_pattern.match(phases) is not None:
        phases = int(phases)
        if check_limits(phases):
            result.append(phases)
            return result
        else:
            raise ValueError(valueErrorMsg)
        
    if interval_pattern.match(phases) is not None: 
        start_phase, end_phase = [int(x) for x in phases.split('-')]
        if (start_phase < end_phase):
                if check_limits(start_phase) & check_limits(end_phase):
                    return list(range(start_phase, end_phase+1))
                else:
                    raise ValueError(valueErrorMsg)
        else:
            raise ValueError(valueErrorMsg)

    raise ValueError(valueErrorMsg)