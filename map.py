from main import parallaxe
from Board import Board


map = []


def init():
    tmp = Board()
    map = tmp.tiles

def display():
    parallaxe()