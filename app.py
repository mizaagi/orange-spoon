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
        filetxt = ""
        if file.filename.endswith(('.mp3', '.ogg', '.wav', '.flac', '.3gp')):
            file.save(f"static/audioFiles/{file.filename}") # Example: audioFiles/samplePlaylist/goodMusic.mp3
            with open(f"static/playlists/{playlist}.txt", "a") as playlisttxt:
                playlisttxt.write(file.filename+"\n")
            with open(f"static/playlists/{playlist}.txt", "r") as playlisttxt:
                filetxt = playlisttxt.read()
            return render_template("fileupload.html", title="File Upload", 
                               message=f"Uploaded file {file.filename} to {playlist} successfully!", filename=f"audioFiles/{playlist}/{file.filename}", filetxt=filetxt.split("\n"))
        else:
            return render_template("fileupload.html", title="File Upload", 
                               message=f"Failed to upload {file.filename}. Please try again with a file with a supported format.")
    return render_template("fileupload.html", title="File Upload")



"""
open("file.txt", 'a').write("songname.mp3")
with open("{{playlistname}}" + ".txt", 'a') # {{playlistname}} get the playlist name from the variable assigned as such
"""

@app.route("/playlists")
def playlists():
    return render_template("playlists.html")

def get_date():
    return datetime.now()

def list_playlists():
    return ["Example Playlist 1", "Example Playlist 2", "Example Playlist 3"]

"""
def new_playlist(playlist_name, contents=[]):
    return render_template("new_playlist.html",
                            title="Playlists",
                            get_date=get_date,
                            list_playlists=list_playlists,
                            playlists=list_playlists())
    playlist = {'name':playlist_name, 'contents':contents}
    # print(playlist['name']) --> playlist_name
    # print(playlist['contents']) --> []
"""


# go to /newplaylist
# today we are making the playlist creation code
# plan is to open folder file using python

#Why not just a txt file with the file names?
#That would be easier

@app.route("/play")
def play():
    files = os.listdir("static/audioFiles")
    return render_template("play.html", title="Play", files=files)