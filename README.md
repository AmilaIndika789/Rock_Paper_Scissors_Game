![Build](https://github.com/AmilaIndika789/Rock_Paper_Scissors_Game/actions/workflows/build_and_test.yml/badge.svg?branch=main&event=push)

[![codecov](https://codecov.io/gh/AmilaIndika789/Rock_Paper_Scissors_Game/graph/badge.svg?token=AQGALYRVOB)](https://codecov.io/gh/AmilaIndika789/Rock_Paper_Scissors_Game)

# Rock Paper Scissors Game

A simple [Rock Paper Scissors](https://wrpsa.com/) game implemented using Python.

## Instructions

1. Install required python dependencies

~~~zsh
pip install -r requirements.txt
~~~


2. Run the following command from the root directory

~~~zsh
python -m src.pkg.rock_paper_scissors src/pkg/rock_paper_scissors.py
~~~


3. [Optional] Run unit tests with coverage and pytest

~~~bash
coverage run --source src.pkg --module pytest --verbose tests
~~~
