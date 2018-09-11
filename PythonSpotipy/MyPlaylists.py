import spotipy
import spotipy.util as util
import os


env = {}

# Read a value from an external file, and store it in the global env map.
def setFromFile(label):
    fileValue = ""
    fileName = label + ".txt"
    try:
        with open(fileName) as f:
            fileValue = f.read()
        f.close
    except :
        print("Failure reading " + label + " file: " + fileName)

    if fileValue:
        env[label] = fileValue
    else :
        print("No " + label + " value read")
        exit()

def showTracks(userid, playlistId):
    playlistTracks = sp.user_playlist(userid, playlistId)
    for t, track in enumerate(playlistTracks['tracks']['items']) :
        print("  %4d  %s" % (t+1, track['track']['name']))

setFromFile('token')
setFromFile('userid')

sp = spotipy.Spotify(auth=env['token'])

playlists = sp.current_user_playlists()

for i, playlist in enumerate(playlists['items']):
    print("%4d %s %s %s" % (i + 1 + playlists['offset'], playlist['owner']['display_name'],  playlist['id'],  playlist['name']))
    showTracks(env['userid'], playlist['id'])

