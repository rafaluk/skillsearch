from utils.utils import calculate_time


class SkillAggregator:
    def __init__(self):
        self.skills = {}

    def process(self, offer_with_skills: list):
        for skill in offer_with_skills:
            if skill in self.skills:
                self.skills[skill] += 1
            else:
                self.skills[skill] = 1
        return self.skills

    @calculate_time
    def process_all_offers(self, offers_with_skills):
        for offer in offers_with_skills:
            self.process(offer.skills)
        return {k: self.skills[k] for k in sorted(self.skills, key=self.skills.get, reverse=True)}
