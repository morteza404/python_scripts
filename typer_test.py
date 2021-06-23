#!/usr/bin/env python3

import typer

def echo(string: str, times: int = typer.Option(1, help="The number of times to echo the string"),
):
    """Echo a string for as long as you like"""

    typer.echo("\n".join([string] * times))

if __name__ == "__main__":
    typer.run(echo)