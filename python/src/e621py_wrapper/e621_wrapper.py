import requests
import json
#import e621_endpoints as e621_endpoints
from . import e621_endpoints
headers = {
    'User-Agent': 'E621 api wrapper',
}
class client:
    def __init__(self):
        self.loggedin = False
        self.username = ""
        self.apikey = ""
        self.clientjson = ""
        self.id = ""
        #add all endpoints
        self.posts = e621_endpoints.posts(self)
        self.pools = e621_endpoints.pools(self)
        self.users = e621_endpoints.users(self)
        self.tags = e621_endpoints.tags(self)
        self.notes = e621_endpoints.notes(self)
        self.util = e621_endpoints.util(self)
        self.wiki = e621_endpoints.wiki(self)
        self.forum = e621_endpoints.forum(self)
    
    def login(self, username, apikey):
        #try user login
        url = "https://e621.net/users/" + username + ".json?login=" + username + "&api_key=" + apikey
        response = requests.get(url, headers=headers).json()
        try:
            if response["success"] == False:
                return(response)
        except:
            self.username = username
            self.apikey = apikey
            self.loggedin = True
            self.clientjson = response
            self.id = response["id"]
            response.update({"success": True})
            return response
