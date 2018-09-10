import spotipy
import spotipy.util as util
import os

token=""
try:
    with open('token.txt') as f:
        token = f.read()
    f.close
except :
    print("Failure to read token file")

if not token:
    print("No token read")
    exit()

userid=""
try:
    with open('userid.txt') as f:
        userid = f.read()
    f.close
except :
    print("Failure to read user ID file")

if not userid:
    print("No userid read")
    exit()

sp = spotipy.Spotify(auth=token)

def showTracks(userid, playlistId):
    playlistTracks = sp.user_playlist(userid, playlistId)
    for t, track in enumerate(playlistTracks['tracks']['items']) :
        print("  %4d  %s" % (t+1, track['track']['name']))

playlists = sp.current_user_playlists()

for i, playlist in enumerate(playlists['items']):
    #print(playlist)
    print("%4d %s %s %s" % (i + 1 + playlists['offset'], playlist['owner']['display_name'],  playlist['id'],  playlist['name']))
    showTracks(userid, playlist['id'])

