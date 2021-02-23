from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>A simple flask app</h1>"


if __name__ == "__main__":
    app.run(debug=True)
