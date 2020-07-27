from time import time
from datetime import datetime


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"> Execution of {func.__name__!r} done in {round(elapsed_time, 2)} seconds.")
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
