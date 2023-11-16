from dataclasses import dataclass
import random
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

    def create_board(self):
        pass
    
    def create_mines():
      mines = []
      mines_number = self.n
      
      for i in range(mines_number)
        mine = [random.randint(self.n,self.m), random.randint(self.n,self.m)]
        mines.append(mine)
      
      return mines
    
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
