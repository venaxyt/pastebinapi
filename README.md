> # PASTEBIN API
```python
# Module originally made by @venaxyt on Github
# Fixed and remodeled by @ksiscute on Github
import pastebinapi

username = "pastebin account username"
password = "pastebin account password"
api_key = "account api_key findable here https://pastebin.com/doc_api"

# Check an account
pastebinapi.check(username, password, api_key)
>>> Output : [username] Valid account

# Get the token of an account
pastebinapi.token(username, password, api_key)
>>> Output : [username] Token : account token

# Upload a paste on an account
privacy = "2"  # 0 : public | 1 : unlisted | 2 : private
content = "That's my text"
title = "ks's paste"
pastebinapi.paste(username, password, api_key, privacy, title, content)
pastebinapi.url(setting="1") # get pastebin url
```

> ### **Install Module** : ``pip install pastebinapi``<br>
