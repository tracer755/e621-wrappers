from distutils.command.upload import upload
from urllib import response
import requests
import json
import shutil
import hashlib
import os
headers = {
    'User-Agent': 'E621 api wrapper (by tracer755)',
}
class posts:
    def __init__(self, clientin):
        self.client = clientin

    def search(self, tags = "", blacklist = "", limit = -1, page = 1, ignorepage = True):
        #prepare tags
        blacklisttags = blacklist.split(" ")
        i = 0
        
        if blacklist != "":
            blacklist = ""
            for tag in blacklisttags:
                blacklist += " -" + tag
                i += 1
        #check to see if page is enforced
        posts = []
        if ignorepage == False:
            #call only the specified page
            url = ""
            if self.client.loggedin == True:
                url = "https://e621.net/posts.json?page=" + str(page) + "&tags=" + tags + blacklist + "&login=" + self.client.username + "&api_key=" + self.client.apikey
            else:
                url = "https://e621.net/posts.json?page=" + str(page) + "&tags=" + tags + blacklist
            response = requests.get(url, headers=headers).json()
            if int(len(response["posts"])) > int(limit):
                i = 0
                while i != limit:
                    posts.append(response["posts"][i])
                    i += 1
            else:
                for items in response["posts"]:
                    posts.append(items)
            return posts
        else:
            pg = page
            i = 0
            posts = []
            while True:
                url = ""
                if self.client.loggedin == True:
                    url = "https://e621.net/posts.json?page=" + str(pg) + "&tags=" + tags + blacklist + "&login=" + self.client.username + "&api_key=" + self.client.apikey
                else:
                    url = "https://e621.net/posts.json?page=" + str(pg) + "&tags=" + tags + blacklist
                response = requests.get(url, headers=headers).json()
                if limit == -1:
                    if len(response["posts"]) == 0 or pg == 750:
                        return posts
                    for item in response["posts"]:
                        i += 1
                        posts.append(item)
                else:
                    if len(response["posts"]) == 0 or pg == 750 or i == limit:
                        return posts
                    for item in response["posts"]:
                        i += 1
                        posts.append(item)
                        if i == limit:
                            return posts
                pg += 1

    def get(self, id):
        if isinstance(id, list) == False:
            id = [id]
        items = []
        for item in id:
            url = ""
            if self.client.loggedin == True:
                url = "https://e621.net/posts.json?&tags=id:" + str(item) + "&login=" + self.client.username + "&api_key=" + self.client.apikey
            else:
                url = "https://e621.net/posts.json?&tags=id:" + str(item)
            response = requests.get(url, headers=headers).json()
            if len(response["posts"]) > 0:
                items.append(response["posts"][0])
        return items
    
    def update(self, tagadd, tagremove):
        print("wip sorry")
    
    def create(self, tags, filepath, rating, sources=[], description = "", parent_id = ""):
        return("wip sorry")
        if self.client.loggedin == False:
            return "login to post"
        source = ""
        for item in sources:
            source += item + "%0A"
        url = "https://e621.net/uploads.json?" + "&login=" + \
            self.client.username + "&api_key=" + self.client.apikey + \
            "&upload[tag_string]=" + tags + "&upload[rating]=" + \
            rating + "&upload[source]" + source + "&upload[description]=" + \
            description + "&upload[parent_id]=" + \
            parent_id + ""
        with open('sp9ols5xzxj71.png', 'rb') as data:
            uploadFile = {'upload[file]': data.read()}

            response = requests.post(url, files=uploadFile, headers=headers)
            return(response.text)

class pools:
    def __init__(self, clientin):
        self.client = clientin

    def search(self, query, limit = -1):
        url = ""
        if limit > -1:
            if self.client.loggedin == True:
                url = "https://e621.net/pools.json?search[name_matches]=" + query + "&limit=" + str(limit) + "&login=" + self.client.username + "&api_key=" + self.client.apikey
            else:
                url = "https://e621.net/pools.json?search[name_matches]=" + query + "&limit=" + str(limit)
        else:
            if self.client.loggedin == True:
                url = "https://e621.net/pools.json?search[name_matches]=" + query + "&login=" + self.client.username + "&api_key=" + self.client.apikey
            else:
                url = "https://e621.net/pools.json?search[name_matches]=" + query
        response = requests.get(url, headers=headers).json()
        return response
    
    def get(self, id):
        items = []
        if isinstance(id, list) == False:
            id = [id]
        for item in id:
            if self.client.loggedin == True:
                url = "https://e621.net/pools.json?search[id]=" + str(item) + "&login=" + self.client.username + "&api_key=" + self.client.apikey
            else:
                url = "https://e621.net/pools.json?search[id]=" + str(item)
            response = requests.get(url, headers=headers).json()
            items.append(response[0])
        return items

class users:
    def __init__(self, clientin):
        self.client = clientin
    def get(self, username):
        if self.client.loggedin == True:
            if username == self.client.username:
                return self.client.clientjson
        url = ""
        url = "https://e621.net/users/" + str(username) + ".json"
        response = requests.get(url, headers=headers).text
        return response
    def favorites(self, userid):
        url = ""
        if self.client.loggedin:
            url = "https://e621.net/favorites.json?user_id=" + str(userid) + "&login=" + self.client.username + "&api_key=" + self.client.apikey
        else:
            url = "https://e621.net/favorites.json?user_id=" + str(userid)
        response = requests.get(url, headers=headers).text
        return response
    
class tags:
    def __init__(self, clientin):
        self.client = clientin
        self.aliases = aliases(clientin)
    
    def search(self, tag, noposts = True):
        url = "https://e621.net/tags.json?search[name_matches]=" + tag + "&search[hide_empty]=" + str(noposts)
        response = requests.get(url, headers=headers).json()
        try:
            a = response["tags"]
            return "No Tags"
        except:
            return response

class aliases:
    def __init__(self, clientin):
        self.client = clientin
    
    def search(self, tag, hideempty = True, status = "", order = ""):
        url = "https://e621.net//tag_aliases.json?search[name_matches]=" + tag + "&search[hide_empty]=" + str(hideempty) + "&search[status]=" + status + "&search[order]=" + order
        response = requests.get(url, headers=headers).json()
        try:
            a = response["tag_aliases"]
            return "No tag aliases"
        except:
            return response

class notes:
    def __init__(self, clientin):
        self.client = clientin

    def search(self, query, wildcard = True, limit = 100):
        if wildcard:
            query = "*" + query + "*"   
        url = "https://e621.net/notes.json?search[body_matches]=" + query + "&limit=" + str(limit)
        response = requests.get(url, headers=headers).json()
        try:
            a = response["notes"]
            return "No notes"
        except:
            return response

    def get(self, post_id, limit = 100):
        url="https://e621.net/notes.json?search[post_id]=" + str(post_id) + "&limit=" + str(limit)
        response = requests.get(url, headers=headers).json()
        try:
            a = response["notes"]
            return "No notes"
        except:
            return response

class wiki:
    def __init__(self, clientin):
        self.client = clientin

    def search(self, query, wildcard=True):
        if wildcard == True:
            query = "*" + query + "*"

        url = "https://e621.net/wiki_pages.json?search[title]=" + query

        response = requests.get(url, headers=headers).json()

        if len(response) == 0:
            return "no wiki"

        return response

    def get(self, id):
        url = "https://e621.net/wiki_pages/" + str(id) + ".json"
        response = ""
        try:
            response = requests.get(url, headers=headers).json()
        except:
            return "no wiki page"
        
        if len(response) == 0:
            return "no wiki page"

        return response

class forum:
    def __init__(self, clientin):
        self.catagories = ["General", "Tag Alias and Implication Suggestions", "Art Talk", "", "Off Topic", "", "", "", "e621 Tools and Applications", "Tag/Wiki Projects and Questions", "Site Bug Reports & Feature Requests"]
        self.client = clientin
    def topics(self, page = 1, catagory = None):
        url = "https://e621.net/forum_topics.json"
        url += "?page=" + str(page)
        if catagory != None and catagory != "":
            tmp = "&search[category_id]=" + str(self.catagories.index(catagory) + 1)
            url += tmp
        response = requests.get(url, headers=headers)
        return response.text
    def posts(self, title = None, body = None, author = None, catagory = None, page = 1):
        url = "https://e621.net/forum_posts.json"
        tmp = "?search[topic_title_matches]="
        if title != None and title != "":
            tmp += title
        url += tmp
        tmp = "&search[body_matches]="
        if body != None and body != "":
            tmp += body
        url += tmp
        tmp = "&search[creator_name]="
        if author != None and author != "":
            tmp += author
        url += tmp
        if catagory != None and catagory != "":
            tmp = "&search[topic_category_id]=" + str(self.catagories.index(catagory) + 1)
            url += tmp
        print(url)

        url += "&page=" + str(page)

        response = requests.get(url, headers=headers)
        
        return(response.text)
        #https://e621.net/forum_posts.json?commit=Search&search[body_matches]=test&search[creator_name]=tset2test2


class util:
    def __init__(self, clientin):
        self.client = clientin

    def save(self, post_id, filepath = "./"):
        post = self.client.posts.get(post_id)
        response = requests.get(post[0]["file"]["url"], headers=headers, stream=True)

        if filepath != "":
            if filepath.endswith('/') == False:
                filepath += "/"
        if filepath != "":
            if os.path.isdir(filepath) == False:
                os.mkdir(filepath)
        if response.status_code == 200:
            filename = str(post[0]["id"]) + "." + post[0]["file"]["url"].split(".")[len(post[0]["file"]["url"].split(".")) - 1]
            response.raw.decode_content = True
            with open(filepath + filename,'wb') as f:
                    shutil.copyfileobj(response.raw, f)

                    if hashlib.md5(open(filepath + filename,'rb').read()).hexdigest() == post[0]["file"]["md5"]:
                        return("File saved to: " + filepath + filename)
                    else: 
                        os.remove(filepath + filename)
                        return("md5 checksum fail please try again")

