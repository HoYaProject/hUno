class Player:
    def __init__(self):
        self.__hands: [str] = []

    def setup(self, player_type: str, cards: [str]):
        self.type = player_type
        self.__hands = cards

    def get_hands(self) -> [str]:
        return self.__hands