from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from datetime import datetime
import json, os

app = Flask(__name__)




@app.route("/", methods=['GET', 'POST'])
def file_upload():
    if request.method == "POST":
        file = request.files['file']
        file.save(f"audioFiles/{file.filename}")
        return render_template("fileupload.html", title="File Upload", 
                               message="Uploaded file successfully!")
    return render_template("fileupload.html", title="File Upload")

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