#!/usr/bin/python3
"""
Python script that starts a web application
"""


from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_session(exception):
    """function to close the session"""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
