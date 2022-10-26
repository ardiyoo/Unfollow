import json
import subprocess
from time import sleep
import requests
import time
import os


clear = lambda: subprocess.call('cls||clear', shell=True)

def WebFormData(sessionID, username):
    headers = {
        'authority': 'i.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': f'sessionid={sessionID}',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'missing',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1BEtv7Nh6-J0Xji8ZOk9JHUbvcYCc97OKyFUASZX2HbUi_',
        'x-instagram-ajax': '1006468538',
    }

    params = {
        'username': f'{username}',
    }

    res = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/', params=params, headers=headers).text

    js = json.loads(res)
    userxs = js['data']['user']['id']
    GetFollowings(sessionID, userxs)

def login(username, Password):
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'mid=YoP0RQALAAHfFr877zkTS5rerXF5; ig_did=C5AEF60C-D0AA-4209-9750-11E701BD008F; dpr=0.8999999761581421; datr=paeoYqg6cQlL0YULqRMdBVSB; ig_direct_region_hint="ASH\\05435210514607\\0541688904984:01f732add90bcbec9e119bafbec14211c59e710ef59e1f17d41972227101bbac2eaef0bd"; shbid="3068\\054285350012\\0541689091177:01f719a660d9177b74ce592b8da74973924d6e00e41305860914096156d5f7f830f9a81e"; shbts="1657555177\\054285350012\\0541689091177:01f75e89cb99894f0a7dd5e8badd7f976e117a25fe8a4bd5ba4d7314f7d265daa0ea96c2"; rur="ODN\\05454106572712\\0541689174562:01f7561fb134a3f175dd033c32f2c7727f2a3e6abe3bb7855cf6b874e0e8371716eb3b3d"; csrftoken=tucHckw8E8XHcViYnLBl5ntXfvONBdRs',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'tucHckw8E8XHcViYnLBl5ntXfvONBdRs',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR30OBbD31eyeQ85TEwyRFLT1_yiTiGlqERm6K1eQPtO4yr6',
        'x-instagram-ajax': 'fb462f0c47ed',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'username': f'{username}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{Password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }

    res = requests.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=data)
    if 'authenticated":true' in res.text or 'userId' in res.text:
        res.headers.update({'X-CSRFToken': res.cookies['csrftoken']})
        print(f"[Successfully Logged In: {username}]")
        print("\n\n")
        sessionID = res.cookies['sessionid']
        WebFormData(sessionID, username)
    elif 'authenticated":false' in res.text or 'userId' in res.text:
        print(f" [Username or Password is Incorrect]")
        input(f"\n [Enter To Exit]")
        exit()
    else:
        print(f" [{res.text}]")
        input(f"\n [Enter To Exit]")
        exit()

def unfollow(username, id, sessionID):
    headers = {
    'authority': 'i.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': f'sessionid={sessionID}',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'missing',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR27-BzAT808G_qRU82pyCtrl7fYvEoSTy-Z5kIdtMSzSy0N',
    'x-instagram-ajax': '1006468538',
    }

    fsc = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{id}/unfollow/',  headers=headers)
    if '{"status":"ok"}' in fsc.text:
        print(f"User: {username} Unfollowed")
    else:
        print(fsc.text)
    
def getinfo(username, id, sessionID):
    headers = {
        'authority': 'i.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': f'sessionid={sessionID}',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'missing',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1BEtv7Nh6-J0Xji8ZOk9JHUbvcYCc97OKyFUASZX2HbUi_',
        'x-instagram-ajax': '1006468538',
    }

    params = {
        'username': f'{username}',
    }

    res = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/', params=params, headers=headers)

    if 'follows_viewer":true' in res.text:
        pass
    elif 'follows_viewer":false' in res.text:
        sleep(3)
        unfollow(username, id, sessionID)
    else:
        print("Idk Man Error: " + res.text)


def GetFollowings(sessionID, userxs):
    headers = {
        'authority': 'i.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': f'sessionid={sessionID}',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'missing',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1BEtv7Nh6-J0Xji8ZOk9JHUbvcYCc97OKyFUASZX2HbUi_',
        'x-instagram-ajax': '1006468538',
    }


    res = requests.get(f'https://i.instagram.com/api/v1/friendships/{userxs}/following/', headers=headers)

    if "Try Again Later" in res.text:
        print("Please Try Again Later")
    else:
        data = json.loads(res.text)
        userxs = data['users']
        for users in userxs:
            lenof = users['username']
            ids = users['pk']
            getinfo(lenof, ids, sessionID)

            
user = input("Enter Username: ")
passw = input("Enter Password: ")

login(user, passw)
