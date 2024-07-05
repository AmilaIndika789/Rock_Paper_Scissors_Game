import mock
import builtins
import sys
sys.path.append("../src")
print(sys.path)

from src.pkg.rock_paper_scissors import *

def test_is_rock():
    assert is_rock(0) == True
    assert is_rock(1) == False
    assert is_rock(2) == False

def test_is_paper():
    assert is_paper(0) == False
    assert is_paper(1) == True
    assert is_paper(2) == False

def test_is_scissors():
    assert is_scissors(0) == False
    assert is_scissors(1) == False
    assert is_scissors(2) == True

def test_is_equal():
    assert is_equal(0, 0) == True
    assert is_equal(1, 1) == True
    assert is_equal(2, 2) == True
    assert is_equal(0, 1) == False
    assert is_equal(0, 2) == False
    assert is_equal(1, 2) == False

def test_mock():
    with mock.patch.object(builtins, 'input', lambda _: 0):
        assert get_user_choice() == 0