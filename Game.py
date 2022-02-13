from Board import Board
from Player import Player
from Property import Property


class Game:
    players: [Player]
    board: Board
    player_pos_to_play: int

    def __init__(self, nbn_players):
        self.players = [Player() for _ in range(nbn_players)]
        self.board = Board()
        self.player_pos_to_play = 0

    def get_tiles(self) -> Property:
        self.player_pos_to_play %= len(self.board.tiles)
        return self.board.tiles[self.players[self.player_pos_to_play]]

    def play(self, dice_val):
        self.players[self.player_pos_to_play].move(dice_val)
        self.player_pos_to_play += 1
        self.player_pos_to_play %= len(self.players)

