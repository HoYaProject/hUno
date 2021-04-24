class Board:
    def __init__(self):
        self.__played: [str] = []

    def setup(self, card: str):
        self.__played.insert(0, card)

    def get_played_card(self) -> str:
        return self.__played[-1]