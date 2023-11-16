from main import Minefield


def test_known_empty_singular_minefield():
    minefield = Minefield(1,1, [(0, 0)])
    assert(minefield.display() == "0")
