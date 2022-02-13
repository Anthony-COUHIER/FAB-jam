from common import Skills
from Player import Player


class Property:
    buy: Skills = None
    cost: Skills = None
    buyed: bool = False
    id: int = 0
    mystery: bool = False
    name: str = ""
    owner: Player = None

    path: str = ""
    x: int = 0
    y: int = 0

    def __init__(self, cost: Skills, buy: Skills, id: int, name: str, path: str, x: int, y: int, mystery=False):
        self.cost = cost
        self.buy = buy
        self.buyed = False
        self.id = id
        self.name = name
        self.path = path
        self.x = x
        self.y = y
        self.mystery = mystery

    def go_on(self) -> bool:
        return not self.buyed

    def __index__(self):
        return self.id

    def buy(self, new_owner):
        self.owner = new_owner
        self.buyed = True
