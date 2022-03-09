import click
from .game import Game, GuessComponent
from typing import Optional, Tuple


class EnumType(click.Choice):
    def __init__(self, enum, case_sensitive=False):
        self.__enum = enum
        super().__init__(
            choices=[item.value for item in enum],
            case_sensitive=case_sensitive,
        )

    def convert(self, value, param, ctx):
        converted_str = super().convert(value, param, ctx)
        return self.__enum(converted_str)


WELCOME = (
    "Welcome to Fiddle Faddle Flop!"
    # 'Fiddle: "i", Faddle: "a", Flop: "a"'
)


@click.group()
def cli():
    """<help message 1>"""


@cli.group()
def play():
    """<help message 2>"""


@play.command()
def guesser():
    """Play the Guesser! The computer will generate a number for you to guess."""
    click.echo(WELCOME)
    game = Game()
    while number := click.prompt(
        f"\nGuess #{len(game.guesses) + 1}", type=click.Tuple((int,) * 3)
    ):
        response = game.guess(number)
        click.echo(" ".join(map(str, response)))
        if (GuessComponent.fiddle,) * 3 == response:
            click.echo(f"You won in {len(game.guesses)} guesses!")
            break


cli()
