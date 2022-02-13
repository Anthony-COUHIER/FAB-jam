from Property import Property
import json


class Board:
    tiles: [Property] = []


    def __init__(self):
        uid = 0
        properties = json.load(open('./properties.json'))
        for p in properties:
            print(p)
            mystery = False
            try:
                mystery = p["mystery"]
            except Exception as e:
                mystery = False
            asset = Property(p["buy"], p["cost"], uid, p["name"], p["texture"]["path"], p["texture"]["x"],
                             p["texture"]["y"], mystery)
            self.tiles.append(asset)
            uid += 1
