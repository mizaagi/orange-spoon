from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from datetime import datetime
import json, os

app = Flask(__name__)




@app.route("/", methods=['GET', 'POST'])
def file_upload():
    if request.method == "POST":
        playlist = "uploadedSongs" # Sets default "playlist" as a simple uploadedSongs folder, not a playlist at all
        file = request.files['file']
        playlist = request.form['playlistname']
        if file.filename.endswith(('.mp3', '.ogg', '.wav', '.flac', '.3gp')):
            file.save(f"audioFiles/{playlist}/{file.filename}") # Example: audioFiles/samplePlaylist/goodMusic.mp3
            return render_template("fileupload.html", title="File Upload", 
                               message=f"Uploaded file {file.filename} to {playlist} successfully!", filename=f"audioFiles/{playlist}/{file.filename}")
        else:
            return render_template("fileupload.html", title="File Upload", 
                               message=f"Failed to upload {file.filename}. Please try again with a file with a supported format.")
    return render_template("fileupload.html", title="File Upload")

@app.route("/play")
def play():
    pass


@app.route("/playlists")
def playlists():
    return render_template("playlists.html", title="Playlists")

def get_date():
    return datetime.now()

def list_playlists():
    return ["Example Playlist 1", "Example Playlist 2", "Example Playlist 3"]

def new_playlist(playlist_name, contents=[]):
    """
    return render_template("new_playlist.html",
                            title="Playlists",
                            get_date=get_date,
                            list_playlists=list_playlists,
                            playlists=list_playlists())
                            """
    playlist = {'name':playlist_name, 'contents':contents}
    # print(playlist['name']) --> playlist_name
    # print(playlist['contents']) --> []
