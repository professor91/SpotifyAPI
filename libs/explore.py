from APILibs.artists import Artist
from APILibs.album import Album
from libs.jsondb import jsdb

class Explore():
    def __init__(self, _token):
        self.token= _token
        self.artists_db= jsdb("./data/artists.json")

    def Artist(self, artistName: str):
        print("fetching")
        artistId= self.artists_db._cacheddata["toexplore"][artistName]
        self.artists_db._cacheddata["exploring"][artistName]= {"id" : artistId}
        del self.artists_db._cacheddata["toexplore"][artistName]

        self.artists_db._cacheddata["exploring"][artistName]["albums"]= Artist(self.token).getAlbums(artistId)
        self.artists_db.dumpdata()

    def Album(self, artistName: str, albumName: str):
        print("fetching")
        albumId= self.artists_db._cacheddata["exploring"][artistName]["albums"][albumName]["id"]

        self.artists_db._cacheddata["exploring"][artistName]["albums"][albumName]["tracks"]= Album(self.token).getTracks(albumId)
        self.artists_db.dumpdata()

    def allAlbums(self, artistName: str):
        print("fetching")
        albums= list(self.artists_db._cacheddata["exploring"][artistName]["albums"].keys())

        for name in albums:
            self.Album(artistName, name)