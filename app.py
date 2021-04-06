from flask import Flask, redirect, url_for, session, render_template

app = Flask(__name__)
app.secret_key = "jcnuTadg273gd3ybd478"


@app.route('/playground')
def playground():
    return render_template("playground.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/')
def root():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
