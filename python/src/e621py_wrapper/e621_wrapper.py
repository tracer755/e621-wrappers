import requests
import json
from .endpoints import e621_endpoints as e621end
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
        self.posts = e621end.posts(self)
        self.pools = e621end.pools(self)
        self.users = e621end.users(self)
        self.tags = e621end.tags(self)
        self.notes = e621end.notes(self)
        self.util = e621end.util(self)
    
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
