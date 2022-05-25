import requests

class User():
    def __init__(self, token: str):
        self.token= token

    # not working- unauthorized error
    def getSelf(self):
        """
        Get detailed profile information about the current user (including the current user's username).
        """
        return requests.get(
            "https://api.spotify.com/v1/me",
            headers={
                'Authorization' : f'Bearer {self.token}'
            }
        ).json()


    def getPlaylists(self, id):
        """
        Get all playlists of a user with given userID.
        """
        return requests.get(
            f"https://api.spotify.com/v1/users/{id}/playlists",
            headers={
                "Authorization" : f'Bearer {self.token}'
            }
        ).json()

    def getSelfArtistsFollowed(self):
        """
        Get the current user's followed artists.
        """
        return requests.get(
            "https://api.spotify.com/v1/me/following?type=artist",
            headers={
                "Authorization" : f'Bearer {self.token}'
            }
        ).json()