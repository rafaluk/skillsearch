from data_model import OfferWithSkills
from utils.utils import calculate_time
import re

class SkillFinder:
    def __init__(self, skills):
        self.skills = skills
        self.offers_with_skills = []

    def find_skills(self, offer):
        return [skill for skill in self.skills if skill in offer]
    
    def get_salary(self, offer):
        pattern = re.compile("""<span data-qa="salaryLbl">.+<\/span>""")
        salary_tag = pattern.findall(offer)
        if salary_tag:
            return salary_tag[0].replace('<span data-qa="salaryLbl">', '').replace('</span>', '')
        return None
    
    def get_posted_by(self, offer):
        pattern = re.compile("""<span itemprop="name">.+<\/span>""")
        salary_tag = pattern.findall(offer)
        if salary_tag:
            return salary_tag[0].replace('<span itemprop="name">', '').replace('</span>', '')
        return None

    @calculate_time
    def get_skills_for_all(self, offers):
        for offer in offers:
            skills_in_offer = self.find_skills(offer.content.lower())
            salary_in_offer = self.get_salary(offer.content)
            posted_by_in_offer = self.get_posted_by(offer.content)
            offer_with_skills = OfferWithSkills(offer.url, offer.position, salary_in_offer, skills_in_offer, posted_by_in_offer)
            self.offers_with_skills.append(offer_with_skills)
        return self.offers_with_skills
