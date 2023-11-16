import random
from dataclasses import dataclass


def create_mines(m, n, mines_number):
    mines = []
    for i in range(mines_number):
        mine = [random.randint(0, m), random.randint(0, n)]
        mines.append(mine)

    return mines


@dataclass
class Field:
    x: int
    y: int
    is_bomb: bool


class Minefield:
    board: list[list[Field]]

    def __init__(self, m, n, bombs) -> None:
        self.m = m
        self.n = n
        self.bombs = bombs

    def create_board(self):
        pass

    @property
    def height(self):
        return 3

    @property
    def width(self):
        return 4

    def get_mine_coordinates(self):
        pass

    def display(self):
        return "0"

    @staticmethod
    def get_display_value(field: Field):
        return "0"


def main():
    minefield = Minefield(2, 2)
    minefield.display()


if __name__ == "__main__":
    main()
