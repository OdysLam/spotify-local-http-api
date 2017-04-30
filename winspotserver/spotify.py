from string import ascii_lowercase
from random import choice
import urllib
import urllib2
import json

# Default port that Spotify Web Helper binds to.

class ApiClient():
    def __init__(self):
        self.port = 4370
        self.default_return_on = ['login', 'logout', 'play', 'pause', 'error', 'ap']
        self.origin_header = {'Origin': 'https://open.spotify.com'}
        self.online = False
    def get_tokens(self):
        try:
            self.oauth_token = self.get_oauth_token()
            self.csrf_token = self.get_csrf_token()
            self.online = True
            return self.online
        except:
            self.online = False
            return self.online #couldn't get csrf token/ spotify is off
            
    def get_json(self,url, params={}, headers={}):
        if params:
            url += "?" + urllib.urlencode(params)
        request = urllib2.Request(url, headers=headers)
        return json.loads(urllib2.urlopen(request).read())
    def generate_local_hostname(self):
        """Generate a random hostname under the .spotilocal.com domain"""
        subdomain = ''.join(choice(ascii_lowercase) for x in range(10))
        return subdomain + '.spotilocal.com'

    def get_url(self,url):
        return "https://%s:%d%s" % (self.generate_local_hostname(), self.port, url)
        
    def get_version(self):
        return self.get_json(self.get_url('/service/version.json'), params={'service': 'remote'}, headers = self.origin_header)

    def get_oauth_token(self):
        return self.get_json('http://open.spotify.com/token')['t']

    def get_csrf_token(self):
        # Requires Origin header to be set to generate the CSRF token.
        return self.get_json(self.get_url('/simplecsrf/token.json'), headers=self.origin_header)['token']

    def pause(self,pause=True):
        params = {
            'oauth': self.oauth_token,
            'csrf': self.csrf_token,
            'pause': 'true' if pause else 'false'
        }
        self.get_json(self.get_url('/remote/pause.json'), params=params, headers=self.origin_header)

    def unpause(self):
           self.pause(pause=False)

    def play(self, spotify_uri):
        params = {
            'oauth': self.oauth_token,
            'csrf': self.csrf_token,
            'uri': spotify_uri,
            'context': spotify_uri,
        }
        self.get_json(self.get_url('/remote/play.json'), params=params, headers=self.origin_header)

    def get_status(self, return_after=59):
        params = {
            'oauth': self.oauth_token,
            'csrf': self.csrf_token,
            'returnafter': return_after,
            'returnon': ','.join(self.default_return_on)
        }
        return self.get_json(self.get_url('/remote/status.json'), params=params, headers=self.origin_header)

