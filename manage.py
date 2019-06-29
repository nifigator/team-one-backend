import os
import click

from flask import Flask
from flask_migrate import Migrate

from config import db, app

from models import Issue

@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        Issue=Issue,
    )

