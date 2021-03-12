from config import *
import spotipy
import spotipy.util as util

class SpotifyCurrentTrack:
    def get_token(self):
        self.token = util.prompt_for_user_token(
            USERNAME, SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

    def create_client(self):
        self.spotify_client = spotipy.Spotify(self.token)

    def get_track(self):
        self.current_track = self.spotify_client.current_user_playing_track()

    def get_song_name(self):
        self.song_name = self.current_track['item']['artists'][0]['name']



