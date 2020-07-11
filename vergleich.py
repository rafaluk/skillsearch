import pandas as pd

offers = pd.read_csv("offers.csv", header=None)
skills = pd.read_csv("skills.csv", header=None)

skills_dict = {i:0 for i in skills.iloc[:, 0]}

for offer in offers.iloc[:, 0]:
    for skill in skills.iloc[:, 0]:
        if skill in offer:
            skills_dict[skill] += 1

print(skills_dict)

df = pd.DataFrame.from_dict(skills_dict, orient='index')