import Property
from common import Skills


class Player:
    skills: Skills
    case: int
    properties: [Property]

    def __init__(self):
        self.skills = Skills(5, 5, 5, 5, 10000, 0)
        self.case = 0
        self.properties = []

    def move(self, nb_case):
        if nb_case > 0:
            self.case += 1
            self.move(nb_case - 1)
            # sleep

    def can_buy(self, asset: Property) -> bool:
        return not (
                    self.skills.love < asset.buy.love and
                    self.skills.health < asset.buy.health and
                    self.skills.illegal < asset.buy.illegal and
                    self.skills.education < asset.buy.education and
                    self.skills.money < asset.buy.money and
                    self.skills.luck < asset.buy.luck
        )

    def buy(self, asset: Property):
        if self.can_buy(asset):
            self.skills.love -= asset.buy.love
            self.skills.health -= asset.buy.health
            self.skills.illegal -= asset.buy.illegal
            self.skills.education -= asset.buy.education
            self.skills.money -= asset.buy.money
            self.skills.luck -= asset.buy.luck
            self.properties.append(asset)

    def cost(self, asset: Property):
        self.skills.love -= asset.cost.love
        self.skills.health -= asset.cost.health
        self.skills.illegal -= asset.cost.illegal
        self.skills.education -= asset.cost.education
        self.skills.money -= asset.cost.money
        self.skills.luck -= asset.cost.luck
