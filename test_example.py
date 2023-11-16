import pytest
from main import Minefield


def test_empty_singular_minefield():
    minefield = Minefield(1,1)
    assert(minefield.display() == "0")
