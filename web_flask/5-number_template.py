#!/usr/bin/python3
""" A python script thats starts a flask web application """
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def hello_bnb():
    """ function that displays Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ function that returns HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """function that takes in args """
    new_text = ""
    for underscore in text:
        if underscore == "_":
            new_text += " "
        else:
            new_text += underscore
    return f"C {new_text}"


@app.route('/python/',  strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text=None):
    """function that prints python with the tecxt variable"""
    if text:
        new_text = ""
        for underscore in text:
            if underscore == "_":
                new_text += " "
            else:
                new_text += underscore
        text = new_text
    else:
        text = "is cool"
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """function that checks if nymber is int"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_template(n=None):
    """function that render a template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
