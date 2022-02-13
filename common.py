from dataclasses import dataclass


@dataclass
class Skills:
    love: int
    education: int
    luck: int
    health: int
    money: int
    illegal: int

    def __init__(self, love=0, education=0, luck=0, health=0, money=0, illegal=0):
        self.love = love
        self.education = education
        self.luck = luck
        self.health = health
        self.money = money
        self.illegal = illegal
