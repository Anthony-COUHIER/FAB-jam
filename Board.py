from Property import Property
import json


class Board:
    tiles: [Property]

    def __init__(self):
        uid = 0
        properties = json.load('./properties.json')
        for p in properties:
            asset = Property(p.buy, p.cost, uid, p.name, p.texture.path, p.texture.x, p.texture.y, p.mystery)
            self.tiles.append(asset)
            uid += 1
