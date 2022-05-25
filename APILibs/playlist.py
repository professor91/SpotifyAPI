import requests

class Playlist():
    def __init__(self, token: str):
        self.token= token

    def get(self, id: str):
        """
        Get a playlist given the playlist id.
        """
        return requests.get(
            f"https://api.spotify.com/v1/playlists/{id}",
            headers={
                "Authorization" : f'Bearer {self.token}'
            }
        ).json()
    
    def getItems(self, id: str):
        """
        Get full details of the items of a playlist given the playlist id.
        """
        return requests.get(
            f"https://api.spotify.com/v1/playlists/{id}/tracks",
            headers={
                "Authorization" : f'Bearer {self.token}'
            }
        ).json()