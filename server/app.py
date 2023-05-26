#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
# registers the index() function with the Flask application instance app
# registration means that a view has been connected to an application instances route
# the @app.route decorator is an instance method that modifies app, creating a rule that requests
# for the base URL(/) should show our index: a page with a header.
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == "__main__":
    app.run(port=5555, debug=True)