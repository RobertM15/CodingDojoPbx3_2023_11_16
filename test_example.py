import pytest
from main import Minefield


<<<<<<< HEAD
def test_foo():
    assert foo() == 42

=======
def test_empty_singular_minefield():
    minefield = Minefield(1,1)
    assert(minefield.display() == "0")
>>>>>>> 3140175faad4cc77ba59e26cb6bdb0ba54a59a1e
