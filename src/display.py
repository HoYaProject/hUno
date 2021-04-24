def display_board(card: str):
    print()
    print("######")
    print(f"# {card} #")
    print("######")


def display_player(cards: [str]):
    print()
    print("----------------------")
    print(">", end="")
    for card in cards:
        print(f" {card}", end="")
    print()