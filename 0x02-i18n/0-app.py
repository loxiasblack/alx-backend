#!/usr/bin/env python3
""" first route with basic html """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ render the first template """
    return render_template('0-index.html')


if __name__ == "__main__":
    """run the app"""
    app.run(host='0.0.0.0', port=5000)
