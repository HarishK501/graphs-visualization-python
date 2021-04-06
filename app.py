from flask import Flask, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "jcnuTadg273gd3ybd478"


@app.route('/')
def home():
    return "<h1>A simple flask app</h1>"


if __name__ == "__main__":
    app.run(debug=True)
