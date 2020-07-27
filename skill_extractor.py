from bs4 import BeautifulSoup
from data_model import Link


class SkillExtractor:
    def __init__(self, skills):
        self.skills = skills

    def get_skill_list(self, filename):
        with open(filename, 'r') as file:
            self.skills = [line.rstrip('\n') for line in file]
        return self.skills

    def find_skills(self, offer):
        for skill in self.skills:
            if
