# How to setup Spotify connection

## Install spotipy

`spotipy` is a python library for Spotify.

```
pip3 install git+https://github.com/plamere/spotipy.git@master
```

## Copy Spotify credentials in config.py

You get these when you add an app to Spotify.

```
CLIENT_ID = ''
CLIENT_SECRET = ''
USERNAME = ''
SCOPE = ''
REDIRECT_URI = ''
```

## Run display_spotify_song.py

`python3 display_spotify_song.py`

By running this script a `.cache-isaacinator` file is created.
This file contains the access token to Spotify.
Without this token you can't make any authorized requests to Spotify.

