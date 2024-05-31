#!/usr/bin/env python3
"""
Creating flask app with babel
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    configuratuons for babel
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE ="UTC"

    
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

app@route("/")
def home() -> str:
    """
    handles the main page url
    """

    return render_template("1-index.html")
