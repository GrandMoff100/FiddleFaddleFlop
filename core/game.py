import random
from typing import Tuple, List
from enum import Enum


class GuessComponent(Enum):
    fiddle: str = "Fiddle"
    faddle: str = "Faddle"
    flop: str = "Flop"

    def __str__(self) -> str:
        return self.value


class Game:
    number: Tuple[int, int, int]
    guesses: List[Tuple[int, int, int]]

    def __init__(self):
        self.number = []
        self.guesses = []
        for _ in range(3):
            while (
                digit := random.randint(1, 9)
            ) in self.number:  # Enforces unique digits
                ...
            self.number.append(digit)

    def guess(self, number: Tuple[int, int, int]) -> List[GuessComponent]:
        self.guesses.append(number)
        components = []
        for guess_digit, answer_digit in zip(number, self.number):
            if guess_digit == answer_digit:
                components.append(GuessComponent("Fiddle"))
            elif guess_digit in self.number:
                components.append(GuessComponent("Faddle"))
            else:
                components.append(GuessComponent("Flop"))
        random.shuffle(components)
        return components
