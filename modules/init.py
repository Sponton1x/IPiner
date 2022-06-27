import typer
from modules.animation import *

app = typer.Typer()

@app.command()
def init():
    load_animation()
    print("Ready for work :)")
