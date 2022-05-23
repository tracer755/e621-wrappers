# E621 python wrapper

Install here: https://pypi.org/project/e621py-wrapper/ or use:  pip install e621py-wrapper

Get started:    

First import the library and create a e621 client
```python
import e621py_wrapper as e621
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

## Users

### Get

This function gets user information based on username or an int of userid

Usage  

```python
client.users.get(username)
```

This username param can be a string of a user id or an int of a user id

#### Example

```python
client.pools.get("t-rexQueen")
```

if you are logged in and call your own username(Not user id!!!) the response will have more data

This would return: https://pastebin.com/mK3tpJug

### Favorites

This function gets a users favorites (assuming they are public) based on user id

Usage  

```python
client.users.favorites(id)
```

Id the id paramater of a user you can user user.get to get user id

#### Example

```python
client.users.favorites(292827)
```

This would return: https://pastebin.com/8fCqfr25


## Tags

### Search

This function gets a tag and ralated info

Usage  

```python
client.tags.search(tag)
```

Tag this is a string of a tag not case sensetive

#### Example

```python
client.tags.search("anthro")
```

This would return: https://pastebin.com/t06QnLFa

## Aliases

### Search

This function gets a tag and ralated info

Usage  

```python
client.tags.aliases.search(Main tag, hide empty, status, order)
```

Main tag this is the tag that you want find all aliases of

hide empty hide all aliases that have no posts (True by default)

status tag status eg: approved, active, pending, deleted, retired, processing, queued

order order to sort the tags eg: status (default), created_at, updated_at, name, or tag_count



Only required param is Main tag

#### Example

```python
client.tags.aliases.search("anthro")
```

This would return: https://pastebin.com/9PV8q5ty

## Notes

### Search

This function gets a note based on query and note content

Usage  

```python
client.notes.search(query, wildcard. limit)
```

Query the string query of the request

Wildcard allows the query to not be the exact text of the full note (True by default)

limit limits the number of notes returned (default 100)



Only required param is query

#### Example

```python
client.notes.search("owo")
```

This would return: https://pastebin.com/WC0DSsuq


### Get

This function gets notes based on a posts id

Usage  

```python
client.notes.get(id, limit)
```

id is an int of a posts id

limit the nuber of notes returned 

#### Example

```python
client.notes.get(2983392)
```

This would return: https://pastebin.com/qg9FqBnX

## Utils

### Save

This function gets a post and downloads the file

Usage  

```python
client.util.save(post_id, filepath)
```

post_id the id of the post

the filepath to save the file to (if left blank the file will save the the current directory)


the downloader checks the md5 check sum provided by e621 returns md5 checksum fail please try again if the check sum fails

#### Example

```python
client.util.save(3178128)
```

This saves the post to the file path 3178128.png

```python
client.util.save(3178128, "test")
```

The file is saved to the path test/3178128.png


## Wiki

### Search

This function searches for wiki pages

Usage  

```python
client.wiki.search(query, wildcard)
```

query the search query for the wiki page

wildcard allows the query to not be exact and be a part of a string (True by default leaving this is recomended)

#### Example

```python
client.wiki.search("wickerbeast")
```

This would return: https://pastebin.com/C3j30QA6

### Get

This function gets a wiki page based on id

Usage  

```python
client.wiki.get(id)
```

id the id of a wiki page

#### Example

```python
client.wiki.get(42470)
```

This would return: https://pastebin.com/BwifkJL0
