#/usr/bin/python

import socket
import typer


@app.command("getPort")
def portScanner(port: int = typer.Option(..., "--port"), host: str = typer.Option(..., "--host")):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

app()
