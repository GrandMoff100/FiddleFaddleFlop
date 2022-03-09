import click

from .game import Game, GuessComponent


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


WELCOME = "Welcome to Fiddle Faddle Flop!"


@click.group()
def cli():
    """Play Fiddle Faddle Flop!"""


@cli.command()
def keeper():
    """Play the keeper! The computer tries to guess your number"""


@cli.command()
def guesser():
    """Play the Guesser! It will generate a number for you to guess"""
    click.echo(WELCOME)
    game = Game()
    while number := click.prompt(
        f"\nGuess #{len(game.guesses) + 1}", type=click.Tuple((int,) * 3)
    ):
        response = game.guess(number)
        click.echo(" ".join(map(str, response)))
        if (GuessComponent.FIDDLE,) * 3 == response:
            click.echo(f"You won in {len(game.guesses)} guesses!")
            break


cli()
