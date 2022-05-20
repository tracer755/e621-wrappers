# E621 python wrapper

Install here: https://pypi.org/project/e621-wrapper/ or use:  pip install e621-wrapper

Get started:    

First import the library and create a e621 client
```python
import e621_wrapper as e621
client = e621.client()
```
  
Now lets login, some api calls will require logging in  
```python
client.login("username", "apikey")
```
Now lets try getting 3 posts with the tag wickerbeast and blacklisting rating:e
```python
print(client.posts.search("wickerbeast", "rating:e", 3))
```

Full docs

## Posts

### Search

This function searches for posts matching the input tags

Usage
```python
client.posts.search(tags, blacklist, limit, page, ignorepage)
```

Tags is the input tags eg: "wickerbeast rating:e" if more than 1 tag is input sepereate the tags by a space

Blacklist is the same as tags but the wrapper will ignore these tags eg: rating:e will get rid of explicit results

Limit the ammount of posts returned

Page page number to start at unless ignorepage is equal to False in which case it will only get posts from the input page

#### Example 

```python
client.posts.search("wickerbeast", "rating:e", 1, 1, False)
```

(All example returns are going to be in paset bin because they are big)  
This would return: https://pastebin.com/Rg8G11Jn 
