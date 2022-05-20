# e621-wrappers
e621 api wrappers for a bunch of languages  

#### Languages
- [x] [Python](python/README.md) (wip)
- [ ] Node js (planned)
- [ ] Js (planned)
- [ ] c# (planned)
- [ ] java (planned)
- [ ] c++ (probably not)

## [Python](python/README.md)
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
Now lets try getting 3 posts with the tag wickerbeast and blacklisting rating:e
```python
print(client.posts.search("wickerbeast", "rating:e", 3))
```
[For full documentation click here](python/README.md)

Todo:  
Post management  
wiki  
forum  
