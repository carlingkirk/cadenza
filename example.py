import yaml
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

if __name__ == '__main__':
    config = yaml.safe_load(open('secrets.yml', 'rt'))
    auth = SpotifyClientCredentials(client_id=config.get('client_id'), client_secret=config.get('client_secret'))
    client = spotipy.Spotify(client_credentials_manager=auth)

    print(client.search('Patrick Lee'))
