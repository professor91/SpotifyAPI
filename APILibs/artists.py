import requests

class Artist():
    def __init__(self, _token: str):
        self.token= _token

    def getArtist(self, id):
        """
        Get Spotify catalog information for a single artist identified by their unique Spotify ID.
        """
        return requests.get(
            f"https://api.spotify.com/v1/artists/{id}",
            headers={
                'Authorization' : f'Bearer {self.token}'
            }
        ).json()
        
    def getAlbums(self, id):
        """
        Get all albums of an artist given artist ID.
        """
        r= requests.get(
            f"https://api.spotify.com/v1/artists/{id}/albums",
            headers={
                'Authorization' : f'Bearer {self.token}'
            }
        )

        # list of all album's ids
        return {x["name"]: {"id": x["id"]} for x in r.json()["items"]}

    def getTopTracks(self, id):
        """
        Get an artist's top tracks by country given artist ID.
        """
        return requests.get(
            f"https://api.spotify.com/v1/artists/{id}/albums",
            headers={
                'Authorization' : f'Bearer {self.token}'
            }
        ).json()