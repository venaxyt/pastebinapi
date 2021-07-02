# Module made by @venaxyt on Github
import requests

def check(username, password, api_key):
    if not username or not password or not api_key:
        raise ValueError("username, password and api key has to be specified.")
    else:
        login_data = {
            "api_dev_key": api_key,
            "api_user_name": username,
            "api_user_password": password,
            }
        login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
        if login.status_code == 200:
            print(f" [{username}] Valid account")
        else:
            print(f" [{username}] Invalid account")

def token(username, password, api_key):
    if not username or not password or not api_key:
        raise ValueError("username, password and api key has to be specified.")
    else:
        login_data = {
            "api_dev_key": api_key,
            "api_user_name": username,
            "api_user_password": password,
            }
        login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
        if login.status_code == 200:
            print(f" [{username}] Token : {login.text}")
        else:
            print(f" [{username}] Invalid account")

# Privacity : 0 (public), 1 (unlisted), 2 (private)
def paste(username, password, api_key, privacity, title, content):
    if not username or not password or not api_key:
        raise ValueError("username, password, api key, privacity code, title and content has to be specified.")
    else:
        login_data = {
            "api_dev_key": api_key,
            "api_user_name": username,
            "api_user_password": password,
            }
        login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
        if not login.status_code == 200:
            print(f" [{username}] Invalid account")
        else:
            data = {
                "api_option": "paste",
                "api_dev_key": api_key,
                "api_paste_code": content,
                "api_paste_name": title,
                "api_paste_expire_date": "N",
                "api_user_key": None,
                "api_paste_format": "php",
                "api_paste_private": privacity,
                }
            paste = requests.post("https://pastebin.com/api/api_post.php", data=data)
            if "https://pastebin.com" in paste.text:
                print(" [>] Successfully uploaded :")
                print(f" [>] Pastebin text page : {paste.text}")
                print(f' [>] Pastebin text /raw : {(paste.text).replace("https://pastebin.com/", "https://pastebin.com/raw/")}')
            else:
                print(f" [>] An error occurred : {paste.text}")
