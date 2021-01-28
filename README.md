
# skillsearch
An ETL tool for searching skills in job offers.

## High level design

to be created

## Installation

1. Clone this project.
2. Install all dependencies: `pip install -r requirements.txt`
3. Download chrome driver: https://chromedriver.chromium.org/downloads (if you don't have it already)
4. In `Config.py` set:
    * path to `chromedriver.exe`s


## Run

Use `run.py` to start the ETL:

    python run.py

### Parameters

* `-p, --phases` - specify the phases to be run, for example:
    * `python run.py -p 1` - runs only first phase
    * `python run.py -p 3` - runs only third phase
    * `python run.py -p 2-4` - runs phases from second to fourth included

