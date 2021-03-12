from spotify_current_track import SpotifyCurrentTrack

track = SpotifyCurrentTrack()
track.get_token()
track.create_client()

track.get_track()
print(track.current_track)
track.get_song_name()
print(track.song_name)