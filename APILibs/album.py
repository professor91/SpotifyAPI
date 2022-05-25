import requests

class Album():
    def __init__(self, _token: str):
        self.token= _token

    def getTracks(self, _id):
        """
        Get Spotify catalog information for a single album.
        """
        r= requests.get(
            f"https://api.spotify.com/v1/albums/{_id}",
            headers={
                'Authorization' : f'Bearer {self.token}'
            }
        )
        
        #list of all tracks
        return {x["name"]: {"id": x["id"]} for x in r.json()["tracks"]["items"]}