import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()
CI = os.getenv("CLIENT_ID")
CS = os.getenv("CLIENT_SECRET")

def addSong(trackURL):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= CI,
                                               client_secret= CS,
                                               redirect_uri="http://localhost/",
                                               scope=["playlist-modify-public", "playlist-modify-private"]))

    # Define the playlist ID and track URI
    playlist_url = "https://open.spotify.com/playlist/1ZEdxOAw2IL5uRFtGZYz9B"

    # Extract the playlist ID from the URL
    playlist_id = playlist_url.split("/")[-1]

    track_url = str(trackURL)

    # Extract the track ID from the URL
    track_id = track_url.split("/")[-1].split("?")[0]

    track_uri = "spotify:track:"+track_id

    # Add the track to the playlist
    sp.playlist_add_items(playlist_id, [track_uri])
    

#addSong('https://open.spotify.com/track/0s76ExpXyMGVBlKLUr683e?si=wHAKYm6BSsa336ItGwYgHA')
