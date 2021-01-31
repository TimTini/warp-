import socks
import socket
from socket import timeout
import urllib.request
import json
import datetime
from datetime import datetime as dt
import random
import string
import time
import os
import sys
def getProxy():
    try:
        socket.socket = _socket
        req         = urllib.request.Request('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=150&country=all')
        response    = urllib.request.urlopen(req)
        proxy_list = response.read().decode('utf-8')
        return proxy_list.split('\r\n')
    except Exception:
        return []
def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)            
def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))    
    except Exception as error:
        print(error)    
def run(proxy_host,t=0):
    try:
        install_id = genString(22)
        body = {"key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                "locale": "es_ES"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                    'Host': 'api.cloudflareclient.com',
                    'Connection': 'Keep-Alive',
                    'Accept-Encoding': 'gzip',
                    'User-Agent': 'okhttp/3.12.1'
                    }
        if(proxy_host != "" and t == 0):
            pro = proxy_host.split(':')
            socks.set_default_proxy(socks.SOCKS4, pro[0], int(pro[1]))
            socket.socket = socks.socksocket
        elif proxy_host == "" and t == 0:
            socket.socket = _socket
        req         = urllib.request.Request(url, data, headers)
        if t > 0:
            response    = urllib.request.urlopen(req,timeout=10)
        else:
            response    = urllib.request.urlopen(req,timeout=3)
        status_code = response.getcode()    
        # print(req.data)
        return status_code
    except Exception:
        # print("")
        # print(error)
        return 500
def loop(pl):
    global g
    global og
    global b  
    global time_start
    wl = []
    for proxy in pl:
        og = g
        for i in range(3):
            result = run(proxy,i)
            if result == 200:
                g += 1
                log(proxy)
                if i == 0 :
                    wl.append(proxy)
            else:
                b += 1
                log(proxy)
                break
        og = g
        if dt.timestamp(dt.now()) - time_start > 18:
            no_proxy = ''
            result = run(no_proxy)
            if result == 200:
                g += 1
                log(no_proxy)
            else:
                b += 1
                log(no_proxy)
            time_start = dt.timestamp(dt.now())
        og = g
    return wl
def log(p):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Boots warp+ id \"{referrer}\" via Socks4")
    if p == '': 
        p = 'Non proxy'
        #index of proxy
        ip = -1
    else:
        ip = proxy_list.index(p)
    running_time = dt.timestamp(dt.now()) - time_pg_start
    print(f"Total time: {int(running_time)}s")
    if running_time > 60:
        per_sc = 60
    else:
        per_sc = running_time
    sg = per_sc * g / running_time
    sb = per_sc * b / running_time
    print(f"Proxy: {p} ({ip + 1}/{len(proxy_list)})")
    print(f"Total:")
    print(f"\tGood : {g} (+{g - og})")
    print(f"\tBad  : {b}")
    print(f"\nSpeed:")
    print(f"\tGood : {int(sg)}/m")
    print(f"\tBad  : {int(sb)}/m")
##################################################################################
# global referrer
# global url
# global _socket
# global no_proxy
# global proxy
referrer = "5fb12dd5-2cd6-474a-ae58-d6bd5ec2f51b"
url      = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
_socket  = socket.socket
g        = 0    #good
b        = 0    #bad
og       = 0    #old good
no_proxy = ''   #khong dung proxy
proxy    = ''   #proxy dang dung
os.system('cls' if os.name == 'nt' else 'clear')    #clear man hinh
#thoi gian quay lại khong can proxy
time_start = dt.timestamp(dt.now())
#thoi gian chay pg
time_pg_start = dt.timestamp(dt.now())
#danh sach proxy
proxy_list=[]
#danh sach proxy dung duoc
while_list=[]
#boost 3 lan
for x in range(3):
    result = run(no_proxy)
    if result == 200:
        g += 1
        log(no_proxy)
    else:
        b += 1
        log(no_proxy)
        break
while True:
    for proxy in proxy_list:
        og = g
        for i in range(3):
            result = run(proxy,i)
            if result == 200:
                g += 1
                log(proxy)
                if i == 0 :
                    while_list.append(proxy)
            else:
                b += 1
                log(proxy)
                break
        og = g
        if dt.timestamp(dt.now()) - time_start > 18:
            no_proxy = ''
            result = run(no_proxy)
            if result == 200:
                g += 1
                log(no_proxy)
            else:
                b += 1
                log(no_proxy)
            time_start = dt.timestamp(dt.now())
        og = g
        if len(while_list) > 9:
            while_list = loop(while_list)
    if len(while_list) > 10:
        proxy_list = while_list.copy()
        while_list = []
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Restore white list {len(while_list)} items')
        proxy_list = while_list.copy()
        print('Getting new proxy . . .')
        #new proxies
        np = getProxy()
        if len(np) == 0 : exit()
        random.shuffle(np)
        proxy_list.extend(np)
        print(f'Merge {len(while_list)} + {len(np)} = {len(proxy_list)}')
        while_list = []
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
