from APILibs.Oauth import Auth
from libs.explore import Explore

from secret import client_id
from secret import client_secret

client= Auth(client_id, client_secret)

token= client.client_credentials_flow()

explore= Explore(token)

# print(explore.Artist("Shawn Mendes"))
# explore.Album("Shawn Mendes", "Wonder")

# explore.Artist("Ritviz")
# explore.Album("Ritviz", "Roshni")