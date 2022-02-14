import pygame

from Board import Board
from Player import Player
from Property import Property
from common import draw_text


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

    def play(self, dice_val, screen, FONT):
        player = self.players[self.player_pos_to_play]
        player.move(dice_val)
        case: Property = Board.tiles[player.case]

        print(case.path)
        print(case.x)
        print(case.y)

        print("buy ", case.buy)
        print("cost ", case.cost)
        print("buyed ", case.buyed)
        print("id ", case.id)
        print("mystery ", case.mystery)
        print("name ", case.name)
        print("owner ", case.owner)
        if not case.buyed:
            if player.can_buy(case):
                player.buy(case)
                case.owner = player
                # draw_text("Do you want to buy it ?, [y/n]", 0, 0, screen, FONT)
                # for e in pygame.event.get():
                #     if e.type == pygame.KEYDOWN:
                #         if e.key == pygame.Y_KEY:
                #         else:
                #             pass
            else:
                draw_text("You can't buy it...", 0, 0, screen, FONT)
        elif case.owner != player:
            player.cost(case)
        print("buy ", case.buy)
        print("cost ", case.cost)
        print("buyed ", case.buyed)
        print("id ", case.id)
        print("mystery ", case.mystery)
        print("name ", case.name)
        print("owner ", case.owner)

        self.player_pos_to_play += 1
        self.player_pos_to_play %= len(self.players)

