from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from datetime import datetime
import json, os

app = Flask(__name__)
new_song = ""

#for
# for (int lcv = 0; lcv <= 500; lcv++) {Console.WriteLine}
@app.route("/", methods = ["GET","POST"])
@app.route("/home", methods = ["GET", "POST"])
def home_page():
    if request.method == "POST":
        audioFile = request.form["audio"]
        fileName = secure_filename(audioFile.filename)
        upload_song(fileName) # Updates AllSongs.txt with filename
        filename = secure_filename(audioFile.filename)
        audioFile.save(os.path.join(app.config['audioFiles/'], filename))
        
        return render_template("index.html", 
                               title="Home", 
                               new_song=new_song, 
                               upload_song=upload_song, 
                               update_song=update_song)

    return render_template("index.html", 
                           title="Home", 
                           new_song=new_song, 
                           upload_song=upload_song, 
                           update_song=update_song)

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

def upload_song(name):
    new_song = name
    with open("AllSongs.txt", "a") as f:
        f.write(new_song + "\n")
    if new_song != "":
        return f"Your song {new_song} was uploaded."
    return ""

def update_song(songname):
    global new_song
    new_song = songname