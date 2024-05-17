from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home_page():
    if request.method == "POST":
        audioFile = request.form["audio"]
        
    return render_template("index.html", title="Home")

@app.route("/playlists")
def playlists():
    return render_template("playlists.html", title="Playlists")

def get_date():
    return datetime.now()

def list_playlists():
    return ["Example Playlist 1", "Example Playlist 2", "Example Playlist 3"]

@app.route("/new_playlist")
def new_playlist():
    return render_template("new_playlist.html",
                            title="Playlists",
                            get_date=get_date,
                            list_playlists=list_playlists,
                            playlists=list_playlists())
