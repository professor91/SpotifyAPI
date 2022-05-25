import requests
import base64

class Auth():

    def __init__(self, client_id: str, client_secret: str):
        self.client_id= client_id
        self.client_secret= client_secret
        self.TOKEN_URL= 'https://accounts.spotify.com/api/token'
        self.AUTH_URL= 'https://accounts.spotify.com/authorize'


    def get_client_credentials(self):
        """
        Return a base64 encoded string
        """
        client_id= self.client_id
        client_secret= self.client_secret
        
        if client_id == None or client_secret == None:
            raise Exception("You must set client_id and client_secret")
        
        client_creds= f"{client_id}:{client_secret}"
        client_credsb64= base64.b64encode(client_creds.encode())

        return client_credsb64.decode()


    # client-credentials
    def client_credentials_flow(self):
        """
        Perform Client Credentials authorization
        """
        client_credsb64= self.get_client_credentials()

        return requests.post(
            self.TOKEN_URL,
            data={'grant_type' : 'client_credentials'},
            headers={'Authorization' : f'Basic {client_credsb64}'}
        ).json()['access_token']


    # authorization code flow - Error 400 for get request
    def auth_code_flow(self):
        """
        Request Autherization code
        """
        r= requests.get(
            self.AUTH_URL,
            data={
                'client_id' : self.client_id,
                'response_type' : 'code',
                'redirect_uri' : 'https://professor91.github.io/keshav-saini/',
                'scope' : 'user-follow-read playlist-modify-public playlist-read-private playlist-modify-private'
            }
        )
        
        if r.status_code not in range(200,299):
            raise Exception(f"User did not authorize {r.reason} {r.status_code}")
        else:
            client_credsb64= self.get_client_credentials()

            return requests.post(
                self.TOKEN_URL,
                data={
                    'grant_type' : 'authorization_code',
                    'code' : r.json()['code'],
                    'redirect_uri' : 'https://professor91.github.io/keshav-saini/'
                },
                headers={
                    'Authorization' : f'Basic {client_credsb64}'
                }
            ).json()['access_token']