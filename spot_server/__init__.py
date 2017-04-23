import spot_server.spotify
from flask import Flask,jsonify
app = Flask('spot_server')
import time 

client = spot_server.spotify.ApiClient()
online = client.get_tokens()
while not online:
    print("offline")
    online  = client.get_tokens()
    time.sleep(1)
print("online")

@app.route('/')
def index():
    return ("Welcome to the spotify server, made my OdysLam")

@app.route('/play/<uri>', methods = ['GET'])
def play_playlist(uri):
    if uri == " ":
        return("Need playlist/song URI string to play. /play/<uri>")
    client.play(uri)
    return ('play: ' + uri)

@app.route('/pause', methods = ['GET'])
def pause_playlist():
    client.pause()
    return ('pause')

@app.route('/unpause', methods = ['GET'])
def unpause():
    client.unpause()
    return ('unpause')
@app.route('/online',methods = ['GET'])
def isonline():
    return client.online
@app.route('/status', methods = ['GET'])
def status():
    st = client.get_status(return_after=1)
    ans = {}
    ans['playing'] = st['playing']
    if ans['playing']:
        ans['track'] = st['track']['track_resource']['name']
        ans['track_uri'] = st['track']['track_resource']['uri']
    return jsonify(ans)
