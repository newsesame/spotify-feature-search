from dotenv import load_dotenv
import os 
import base64

from requests import post
from requests import get
import json


load_dotenv()


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


playlist = {
    "2025_Sept": "4EZjmY2sYolhizgGEedVZS"
}


# print(client_secret)



def get_token():
    
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = 'https://accounts.spotify.com/api/token'
    headers = {

        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data = {"grant_type": 'client_credentials'}

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)

    return json_result["access_token"]

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}



def get_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def get_album(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def get_track(token, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result


def get_tracks(token, track_ids):
    url = f"https://api.spotify.com/v1/tracks"

    url = url + "?ids=" + ",".join(track_ids)

    headers = get_auth_header(token)
    result = get(url, headers=headers, data=track_ids)
    json_result = json.loads(result.content)
    return json_result


def playlist_to_track_ids(playlist):
    return [item["track"]["id"] for item in playlist["tracks"]["items"]]



# t(get_token())
playlist= get_playlist(get_token(), playlist["2025_Sept"])
print(playlist)


# playlist_track_ids = playlist_to_track_ids(playlist)
# print(playlist_track_ids)

# tracks = get_tracks(get_token(), playlist_track_ids)
# print(tracks)








