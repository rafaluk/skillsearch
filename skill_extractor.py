from data_model import OfferWithSkills
from utils.utils import calculate_time


class SkillExtractor:
    def __init__(self, skills):
        self.skills = skills
        self.offers_with_skills = []

    def find_skills(self, offer):
        return [skill for skill in self.skills if skill in offer]

    @calculate_time
    def get_skills_for_all(self, offers):
        for offer in offers:
            skills_in_offer = self.find_skills(offer.content)
            offer_with_skills = OfferWithSkills(offer.url, offer.position, skills_in_offer)
            self.offers_with_skills.append(offer_with_skills)
        return self.offers_with_skills
