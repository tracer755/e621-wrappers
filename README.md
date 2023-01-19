# e621-wrappers
e621 api wrappers for a bunch of languages  

My dumbass made this to get sfw wallpapers lol. Programming, making a 1 day job a 2 month job lmao

#### Languages
- [x] [Python](python)
- [ ] Node js (started)
- [ ] Js (planned)
- [ ] c# (planned)
- [ ] java (started)
- [ ] c++ (probably not)


## [Python](python)
[![Downloads](https://static.pepy.tech/personalized-badge/e621py-wrapper?period=month&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/e621py-wrapper)

Install here: https://pypi.org/project/e621py-wrapper/ or use:  pip install e621py-wrapper

Get started:    

First import the library and create a e621 client
```python
import e621py_wrapper as e621
client = e621.client()
```
  
<br />
  
Now lets login, some api calls will require logging in  
```python
client.login("username", "apikey")
```

<br />

Now lets try getting 3 posts with the tag wickerbeast and blacklisting rating:e
```python
print(client.posts.search("wickerbeast", "rating:e", 3))
```
[For full documentation click here](python/README.md)

Todo:  
Post management  
