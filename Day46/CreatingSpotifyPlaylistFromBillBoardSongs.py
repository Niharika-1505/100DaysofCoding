import os

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

""" Documentation for spotify search API: https://developer.spotify.com/documentation/web-api/reference/#/
operations/search"""

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url="https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, "html.parser")
all_songs = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                       "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                       "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330"
                                       " u-max-width-230@tablet-only",
                          id="title-of-a-story")
first_song = soup.find("h3", class_="c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max "
                                    "lrv-u-color-black u-color-white@mobile-max lrv-u-margin-r-150",
                       id="")
songs_list = [first_song.get_text().replace("\n", "")]
for songs in all_songs:
    songs_list.append(songs.getText().replace("\n", ""))

# Spotify Authentication...Added Client_id and Client_Secret to environment variables in edit configurations
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",  # Make sure this link and link added in spotify project settings are
        # the same.
        client_id=os.environ["SPOTIFY_CLIENTID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
# After writing the code until above line, execute it..in order to generate token.txt and also
# authenticate spotify successfully

# Searching spotify for songs by Title
song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
