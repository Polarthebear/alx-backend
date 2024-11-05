#!/usr/bin/env python3
"""
Basic Flask Route
"""

from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Class replresenting babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'])
def index():
    """Hello World"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)