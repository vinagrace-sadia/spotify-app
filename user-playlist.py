import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Whoops, need a username!")
#     print("usage: python user_playlists.py [username]")
#     sys.exit()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

playlists = sp.user_playlists('vinachaider')
pprint(playlists)

# for playlist in playlists['items']:
#     print(playlist['name'])