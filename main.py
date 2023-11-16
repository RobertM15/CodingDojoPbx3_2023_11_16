import random
from dataclasses import dataclass


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
        for row in range(0, self.m):
            for col in range(0, self.n):
                self.board[row][col] = Field(row, col, False)

    @property
    def height(self):
        return 3

    @property
    def width(self):
        return 4


    def create_mines(self):
        mines = []
        mines_number = self.n

        for i in range(mines_number):
            mine = [random.randint(self.n, self.m), random.randint(self.n, self.m)]
            mines.append(mine)

        return mines

    def get_mine_coordinates(self):
        pass

    def display(self):
        if self.board[0, 0].is_bomb:
            return "*"
        else:
            return "0"

    @staticmethod
    def get_display_value(field: Field):
        if field.is_bomb:
            return "*"
        return ""


def main():
    minefield = Minefield(2, 2, [])
    minefield.display()


if __name__ == "__main__":
    main()
