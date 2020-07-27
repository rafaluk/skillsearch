from dataclasses import dataclass


@dataclass
class Link:
    url: str
    position: str


@dataclass
class Offer:
    url: str
    position: str
    content: str


@dataclass
class OfferWithSkills:
    url: str
    position: str
    skills: list

