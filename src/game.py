from defines import *
from board import Board
from card import Card
from player import Player


class Game:
    def __init__(self):
        self.card = Card()
        self.board = Board()
        self.players = []

    def setup(self, num_player: int, player_idx: int):
        self.card.setup()

        for i in range(num_player):
            player = Player()
            if i == player_idx:
                player.setup(PLAYER_TYPE_HUMAN, self.card.get_from_dummy(7))
            else:
                player.setup(PLAYER_TYPE_COM, self.card.get_from_dummy(7))
            self.players.append(player)

        while True:
            start_card: str = self.card.get_from_dummy(1)[0]
            if "1" <= start_card[1] <= "9":
                self.board.setup(start_card)
                break
            else:
                self.card.add_to_dummy(start_card)
