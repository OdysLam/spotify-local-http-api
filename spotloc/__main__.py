import spotloc.spotify
from flask import Flask,jsonify
import time
app = Flask('spotloc')

@app.route('/')
def index():
    return ("Welcome to the spotify server, made my OdysLam")
@app.route('/play')
@app.route('/play/<uri>', methods = ['GET'])
def play_playlist(uri=None):
    if not uri:
        return("<p>Need playlist/song URI string to play.</p><p>format: ip:port/play/uri_link</p>")
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
        ans['artist'] = st['track']['artist_resource']['name']
        ans['album'] = st['track']['album_resource']['name']
    return jsonify(ans)
@app.errorhandler(404)
def page404(e):
    return("That command doesn't exist, please read the docs")
if __name__ == "__main__":
    client = spotloc.spotify.ApiClient()
    online = client.get_tokens()
    while not online:
        print("Spotify Server is offline")
        online  = client.get_tokens()
        time.sleep(1)
    print("Spotify Server is Online")
    print("Starting Flask Server....")
    app.run(host='0.0.0.0',port=5000)
