from bs4 import BeautifulSoup


class Obrabiacz:

    def __init__(self, input):
        self._input = input

    def extract_lists_from_offers(self):
        offTable = BeautifulSoup(self._input, features="html.parser")
        offTable = offTable.find("table", {"id": "offTable"})
        description = offTable.find("div", {"id": "description"})
        if description is None:
            description = offTable.find_all("div", {"id":"desc"})
            lista_desc = []
            for desc in description:
                desc = desc.find_all("li")
                lista_desc.append(desc)
        else:
            description = description.find_all("li")
        description = [str(i).lower().replace("<li>", " ") for i in description]
        return description

    def check_skill(self, skill):
        return skill in self
