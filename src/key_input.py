import random


def input_player_total() -> int:
    while True:
        try:
            num: int = _get_int_number(f"Input Total Players (2-10): ")
            if 2 <= num <= 4:
                return num
        except:
            continue


def input_player_index() -> int:
    while True:
        try:
            idx: int = _get_int_number(
                f"Input Player Index (If index is not available, COM only play): "
            )
            return idx
        except:
            continue


def _get_int_number(msg: str) -> int:
    try:
        return int(input(msg))
    except:
        raise Exception("Not available")
