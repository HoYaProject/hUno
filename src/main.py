from key_input import *
from display import *
from game import Game

if __name__ == "__main__":
    print("Hello Uno\n")

    game = Game()

    player_total = input_player_total()
    player_idx = input_player_index()
    game.setup(player_total, player_idx)

    display_board(game.board.get_played_card())
    display_player(game.players[0].get_hands())
