from common import Skills


class Property:
    buy: Skills
    cost: Skills
    buyed: bool
    id: int
    mystery: bool
    name: str

    def __init__(self, cost: Skills, buy: Skills, id: int, name: str, mystery=False):
        self.cost = cost
        self.buy = buy
        self.buyed = False
        self.id = id
        self.name = name
        self.mystery = mystery


    def go_on(self) -> bool:
        return not self.buyed

    def __index__(self):
        return self.id
