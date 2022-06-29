import spotipy, os
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# Environment Variables
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

# Spotify Authentication
scope = 'playlist-read-private'
userName = 'vinachaider'
clientAuthManager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# userAuthManager = SpotifyOAuth(scope=scope)
# userAuthManager = spotipy.Spotify(auth_manager=SpotifyOAuth())

spotifyClient = spotipy.Spotify(auth_manager = clientAuthManager)
spotifyUser = spotipy.Spotify(auth_manager = SpotifyOAuth())

# Playlist Query
playlists = spotifyUser.user_playlists(userName, 30)

for playlist in playlists['items']:
    print(playlist['name'])

# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = spotifyUser.next(playlists)
#     else:
#         playlists = None

# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])


## CLASS EXAMPLE
# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()