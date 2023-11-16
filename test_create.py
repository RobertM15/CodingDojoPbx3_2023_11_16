from main import Minefield


def test_create():
    minefield = Minefield(3, 4, [])
    assert minefield.height == 3
    assert minefield.width == 4

