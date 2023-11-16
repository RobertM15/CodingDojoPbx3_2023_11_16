import pytest

from main import create_mines


def test_create_mines():
    mines = create_mines(3, 5, 7)
    assert len(mines) == 7

def test_overload_board_with_mines():
    with pytest.raises(ValueError, match="Too many mines"):
        mines = create_mines(2, 2, 7)
