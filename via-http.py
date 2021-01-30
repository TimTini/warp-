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
        req         = urllib.request.Request('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=4000&country=all&ssl=all&anonymity=all')
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
            socks.set_default_proxy(socks.HTTP, pro[0], int(pro[1]))
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
def log(p):
    os.system('cls' if os.name == 'nt' else 'clear')
    if p == '': p = 'Non proxy'
    running_time = dt.timestamp(dt.now()) - time_pg_start
    sys.stdout.write(f"Total time: {int(running_time)}s")
    if running_time > 60:
        per_sc = 60
    else:
        per_sc = running_time
    sg = per_sc * g / running_time
    sb = per_sc * b / running_time
    if (g > og):
        sys.stdout.write(f"\nProxy: {p} (+{g - og})")
    else:
        sys.stdout.write(f"\nProxy: {p}")
    sys.stdout.write(f"\nTotal: {g} Good {b} Bad")
    sys.stdout.write(f"\nSpeed:")
    sys.stdout.write(f"\tGood: {int(sg)}/m\n\tBad : {int(sb)}/m")
##################################################################################
global referrer
global url
global _socket
global g
global b
global no_proxy
global proxy
referrer = "5fb12dd5-2cd6-474a-ae58-d6bd5ec2f51b"
url      = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
_socket  = socket.socket
g        = 0
b        = 0
og       = 0
no_proxy = ''
proxy    = ''
os.system('cls' if os.name == 'nt' else 'clear')
time_start = dt.timestamp(dt.now())
time_pg_start = dt.timestamp(dt.now())
for x in range(3):
    result = run(no_proxy)
    if result == 200:
        g += 1
        log(no_proxy)
    else:
        b += 1
        log(no_proxy)
        break
og = g
proxy_list=[]
while_list=[]
while True:
    random.shuffle(proxy_list)
    for proxy in proxy_list:
        for i in range(3):
            result = run(proxy,i)
            if result == 200:
                g += 1
                log(proxy)
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
    if len(while_list) > 10:
        proxy_list = while_list.copy()
        while_list = []
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Getting new proxy . . .')
        proxy_list = while_list.copy()
        proxy_list.extend(getProxy())
        while_list = []
        os.system('cls' if os.name == 'nt' else 'clear')
