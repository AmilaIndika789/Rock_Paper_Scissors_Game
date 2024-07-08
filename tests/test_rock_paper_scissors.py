import mock
import builtins
import sys

sys.path.append("../src")
print(sys.path)

from src.pkg.rock_paper_scissors import *


def test_is_rock_when_choice_is_rock():
    assert is_rock(choice=0) == True


def test_is_rock_when_choice_not_rock():
    assert is_rock(choice=1) == False
    assert is_rock(choice=2) == False


def test_is_paper_when_choice_is_paper():
    assert is_paper(choice=1) == True


def test_is_paper_when_choice_not_paper():
    assert is_paper(choice=0) == False
    assert is_paper(choice=2) == False


def test_is_scissors_when_choice_is_scissors():
    assert is_scissors(choice=2) == True


def test_is_scissors_when_choice_not_scissors():
    assert is_scissors(choice=0) == False
    assert is_scissors(choice=1) == False


def test_is_equal_when_equal():
    assert is_equal(0, 0) == True
    assert is_equal(1, 1) == True
    assert is_equal(2, 2) == True


def test_is_equal_when_not_equal():
    assert is_equal(0, 1) == False
    assert is_equal(0, 2) == False
    assert is_equal(1, 2) == False


def test_is_invalid_for_valid_choices():
    assert is_invalid(0) == False
    assert is_invalid(1) == False
    assert is_invalid(2) == False


def test_is_invalid_for_invalid_choices():
    assert is_invalid(242) == True
    assert is_invalid(-5) == True
    assert is_invalid(2.5) == True
    assert is_invalid(-4.5) == True


def test_get_invalid_user_choice(capsys):
    with mock.patch.object(builtins, "input", lambda _: "242"):
        _ = get_user_choice()
        captured = capsys.readouterr()
        assert captured.out == "You typed an invalid input. You lose\n"


def test_get_valid_user_choice():
    with mock.patch.object(builtins, "input", lambda _: "1"):
        valid_user_choice = get_user_choice()
        assert valid_user_choice == 1


def test_find_winner_user_is_rock_computer_is_paper(capsys):
    find_winner(0, 1)
    captured = capsys.readouterr()
    assert captured.out == "You lose\n"


def test_find_winner_user_is_rock_computer_is_scissors(capsys):
    find_winner(0, 2)
    captured = capsys.readouterr()
    assert captured.out == "You win!\n"


def test_find_winner_user_is_paper_computer_is_rock(capsys):
    find_winner(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "You win!\n"


def test_find_winner_user_is_paper_computer_is_scissor(capsys):
    find_winner(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "You lose\n"


def test_find_winner_user_is_scissor_computer_is_rock(capsys):
    find_winner(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "You lose\n"


def test_find_winner_user_is_scissor_computer_is_paper(capsys):
    find_winner(2, 1)
    captured = capsys.readouterr()
    assert captured.out == "You win!\n"


def test_find_winner_user_and_computer_equal(capsys):
    find_winner(0, 0)
    find_winner(1, 1)
    find_winner(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "It's a draw\nIt's a draw\nIt's a draw\n"
