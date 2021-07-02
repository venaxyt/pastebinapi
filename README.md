> # pastebinapi

```
# Module made by @venaxyt on Github
import pastebinapi

username = "pastebin account username"
password = "pastebin account password"
api_key = "account api_key findable here https://pastebin.com/doc_api

# Check an account
pastebinapi.check(username, password, api_key)
>>> Output : [username] Valid account

# Get the token of an account
pastebinapi.token(username, password, api_key)
>>> Output : [username] Token : account token

# Upload a paste on an account
privacity = "2"  # 0 : public | 1 : unlisted | 2 : private
content = "That's my text"
title = "Venax paste"
pastebinapi.paste(username, password, api_key, privacity, title, content)
>>> Output : [>] Successfully uploaded :
>>> Output : [>] Pastebin text page : https://pastebin.com/pasteid
>>> Output : [>] Pastebin text /raw : https://pastebin.com/raw/pasteid
```

> **Download** : ``pip install pastebinapi``<br>
> **PyPi [0.0.3] : https://pypi.org/project/pastebinapi**
