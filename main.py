from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import Secret


def get_playlist():
    credenciales = Secret.SP_credenciales()

    sp = Spotify(auth_manager=SpotifyOAuth(
        client_id=credenciales.client_id,
        client_secret=credenciales.client_secret,
        redirect_uri='http://localhost:8888/callback',
        scope='playlist-read-private'
    ))

    playlist_id = '4hBQnHCl0tL27O6d54s7qq'
    playlist = sp.playlist(playlist_id)

    lista_canciones = []

    for track in playlist['tracks']['items']:
        track_info = track['track']
        track_name = track_info['name']
        artists = track_info['artists']
        artist_names = [artist['name'] for artist in artists]

        info = {
            'Canción': track_name,
            'Artistas': artist_names
        }

        lista_canciones.append(info)

    return lista_canciones


def print_lista(lista_print):
    for i in lista_print:
        print(f'Canción: {i["Canción"]}')
        print(f'Artistas: {", ".join(i["Artistas"])}')
        print()


def create_playlist():
    credenciales = Secret.YT_credenciales()
    youtube = googleapiclient.discovery.build(
        serviceName='youtube',
        version='v3',
        credentials=credenciales.csf
    )


def add_playlist(playlist):
    print("Hello world!")


if __name__ == "__main__":
    lista = get_playlist()
    print_lista(lista)
