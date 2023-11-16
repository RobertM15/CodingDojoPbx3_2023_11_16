from dataclasses import dataclass
from itertools import product


@dataclass
class Field:
    x: int
    y: int
    is_bomb: bool


class Minefield:
    board: list[list[Field]]

    def __init__(self, m, n) -> None:
        self.m = m
        self.n = n
        self.create()

    def create(self):
        mines_coordiantes = self.get_mine_coordinates()
        pass

    def get_mine_coordinates(self):
        pass


    def display(self):
        return "0"

    @staticmethod
    def get_display_value(field: Field):
        pass


def main():
    minefield = Minefield(2, 2)
    minefield.display()


if __name__ == "__main__":
    main()
