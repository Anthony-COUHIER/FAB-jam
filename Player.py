from time import sleep

import pygame

import Property
from common import Skills


class Player:
    skills: Skills = None
    case: int = None
    properties: [Property] = []
    pos = [
        [720, 50], [830, 100], [940, 150], [1050, 200], [1160, 250], [1270, 300], [1380, 350],
        [1270, 400], [1160, 450], [1050, 500], [940, 550], [830, 600], [720, 650],
        [610, 600], [500, 550], [390, 500], [280, 450], [170, 400], [60, 350],
        [170, 300], [280, 250], [390, 200], [500, 150], [610, 100]
    ]
    path: str = ""
    image: pygame.image

    @property
    def x(self):
        return self.pos[self.case][0]

    @property
    def y(self):
        return self.pos[self.case][1]

    def __init__(self, path):
        self.skills = Skills(5, 5, 5, 5, 10000, 0)
        self.case = 0
        self.properties = []
        self.path = path
        self.image = pygame.image.load(self.path)

    def move(self, nb_case):
        if nb_case > 0:
            self.case += 1
            #sleep(1)
            self.case %= 24
            self.move(nb_case - 1)

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
