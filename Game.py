from Board import Board
from Player import Player
from Property import Property


class Game:
    players: [Player] = []
    board: Board = None
    player_pos_to_play: int = 0

    def __init__(self):
        self.players = []
        self.board = Board()
        self.player_pos_to_play = 0

    def create_players(self, nb, paths):
        self.players = [Player(paths[i]) for i in range(nb)]

    def get_tiles(self) -> Property:
        self.player_pos_to_play %= len(self.board.tiles)
        return self.board.tiles[self.players[self.player_pos_to_play]]

    def play(self, dice_val):
        self.players[self.player_pos_to_play].move(dice_val)
        self.player_pos_to_play += 1
        self.player_pos_to_play %= len(self.players)

