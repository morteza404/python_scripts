#!/usr/bin/env python3

import typer

def echo(name: str = typer.Option("hello", "-n", "--name"), times: int = typer.Option(1, "-t", "--times" ,help="The number of times to echo the string"),
):
    """Echo a string for as long as you like"""

    typer.echo("\n".join([name] * times))

if __name__ == "__main__":
    typer.run(echo)