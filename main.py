import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='7a737338055f4456a14896dfa21b63ca',
        client_secret='f921c8aaff2f483080ae2383d94e23ce',
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


def add_playlist(playlist):

    print("Hello world!")


if __name__ == "__main__":
    lista = get_playlist()
    print_lista(lista)
