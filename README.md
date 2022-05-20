# e621-wrappers
e621 api wrappers for a bunch of languages  

## [Python](python/README.md)
Install here: https://pypi.org/project/e621-wrapper/    
Get started:    

First import the library and create a e621 client
```python
import e621_wrapper as e621
client = e621.client()
```
<br>
Now lets try to login, some api calls will require logging in
```python
client.login("username", "apikey")
```
<br>

Todo:  
Post management  
wiki  
forum  
