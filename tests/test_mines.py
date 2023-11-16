from main import create_mines


def test_create_mines():
    mines = create_mines(3, 5, 7)

    assert len(mines) == 7