import os
import codecs
import typer
from typing import List
from typing_extensions import Annotated
from . import app
from .. import get_lines


def write(path, s):
    path = os.path.abspath(os.path.expanduser(path))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with codecs.open(path, 'w', encoding='utf-8') as f:
        f.write(s)


@app.command()
def make(path, full: bool = True, sep: bool = False):
    write(path, get_lines(full, sep))


@app.command()
def index(path, names: Annotated[List[str], typer.Argument()] = None):
    write(os.path.join(path, 'index.html'), s='\n'.join(f"""<div><a href="./{p}">{p}</a></div>""" for p in names or []))


def main():
    app()
