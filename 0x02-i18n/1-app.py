#!/usr/bin/env python3
""" new introduction to config class """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ the class Config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """ render 1-index"""
    return render_template('1-index.html')


if __name__ == "__main__":
    """ run app """
    app.run(host='0.0.0.0', port=5000)
