# How to run this app on Raspberry Pi?

## Setup the Spotify connection

As explained [in this doc](./how-to-setup-spotify-connection.md).

## Copy the cached token to Raspberry Pi

`scp .cache-isaacinator pi@{pi address}:{folder containing app code}`

## Copy app code to Raspberry pi

`scp -r * pi@{pi address}:{folder containing app code}`

This will some unneeded files (e.g. README) . If you want to avoid excessive transfers, delete the local `venv ` folder first.

## SSH into Raspberry Pi

`ssh pi@{pi address}`

## Launch script

Run this script on the Raspberry Pi itself:

`python3 song_spotify_pi.py`