from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", title="Home")

@app.route("/playlists")
def playlists():
    return render_template("playlists.html", title="Playlists")
