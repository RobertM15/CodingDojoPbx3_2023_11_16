from itertools import product


class Field:
    def __init__(self, x, y, is_mine) -> None:
        self.x = x
        self.y = y
        self.is_mine = is_mine


class Minefield:
    board: list[list[Field]]

    def __init__(self, m, n) -> None:
        self.m = m
        self.n = n
        self.create()

    def create(self):
        pass

    def get_mine_coordinates(self):
        pass

    def display(self):
        pass

    @staticmethod
    def get_display_value(field: Field):
        pass


def main():
    print("This is the main function.")


if __name__ == "__main__":
    main()
