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

Limit the ammount of posts returned if Limit is -1 unlimited posts are returned

Page page number to start at unless ignorepage is equal to False in which case it will only get posts from the input page


The only required data to passed into the function id tags


#### Example 

```python
client.posts.search("wickerbeast", "rating:e", 1, 1, False)
```

(All example returns are going to be in paset bin because they are big)  
This would return: https://pastebin.com/zPsSrufT

### Get

This function gets posts from their id

Usage
```python
client.posts.get(id)
```

Id the id of a post eg: 3061292 You can get post id's from the search function

#### Example

```python
client.posts.get(3061292)
```

This would return: https://pastebin.com/xEuw4ND9

## Pools

### Search

This function searches for pools whose titles contain a search query

Usage  

```python
client.pools.search(query, limit)
```

Query search for pools containing the query string

limit limits the ammount of results -1 allows all results

#### Example

```python
client.pools.search("dragon", 10)
```

This would return: https://pastebin.com/9a9QehQ7

### Get

This function searches for pools whose titles contain a search query

Usage  

```python
client.pools.get(id)
```

Id the id of the pool, can be obtained from the pools.search function

#### Example

```python
client.pools.get(20198)
```

This would return: https://pastebin.com/8WQrBcvX
