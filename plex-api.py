from plexapi.server import PlexServer
from plexapi.myplex import MyPlexAccount
baseurl = 'http://river.local:32400'
token = 'Eeu-HQiN8bVWWEHhhFFM'
server = PlexServer(baseurl, token)
account = MyPlexAccount(token)
plex = account.resource('river').connect()
print("plex started")
