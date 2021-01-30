import socks
import socket
from socket import timeout
import requests
import urllib.request
import json
import datetime
from datetime import datetime as dt
import random
import string
import time
import os
import sys
referrer = "5fb12dd5-2cd6-474a-ae58-d6bd5ec2f51b"
_socket = socket.socket
def getProxy():
    try:
        req         = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=4000&country=all')
        proxy_list = req.text
        return proxy_list.split('\r\n')
    except Exception as error: 
        print(error)
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
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run(proxy_host):
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
        if(proxy_host != ""):
            pro = proxy_host.split(':')
            socks.set_default_proxy(socks.SOCKS5, pro[0], int(pro[1]))
            socket.socket = socks.socksocket
        else:
            socket.socket = _socket
        req         = urllib.request.Request(url, data, headers)
        response    = urllib.request.urlopen(req,timeout=5)
        status_code = response.getcode()    
        # print(req.data)
        return status_code
    except Exception:
        # print("")
        # print(error)
        return 500
def log(g,b,p):
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
    sys.stdout.write(f"\nProxy: {p}")
    sys.stdout.write(f"\nTotal: {g} Good {b} Bad")
    sys.stdout.write(f"\nSpeed:")
    sys.stdout.write(f"\tGood: {int(sg)}/m\n\tBad : {int(sb)}/m")
g = 0
b = 0
os.system('cls' if os.name == 'nt' else 'clear')
time_start = dt.timestamp(dt.now())
time_pg_start = dt.timestamp(dt.now())
for x in range(3):
    no_proxy = ''
    result = run(no_proxy)
    if result == 200:
        g += 1
        log(g,b,no_proxy)
    else:
        b += 1
        log(g,b,no_proxy)
        break
proxy_list=[]
while_list=[]
while True:
    random.shuffle(proxy_list)
    for proxy in proxy_list:
        for i in range(3):
            result = run(proxy)
            if result == 200:
                g += 1
                log(g,b,proxy)
                while_list.append(proxy)
            else:
                b += 1
                log(g,b,proxy)
                break
        if dt.timestamp(dt.now()) - time_start > 60:
            for j in range(3):
                no_proxy = ''
                result = run(no_proxy)
                if result == 200:
                    g += 1
                    log(g,b,no_proxy)
                else:
                    b += 1
                    log(g,b,no_proxy)
            time_start = dt.timestamp(dt.now())
    if len(while_list) > 10:
        proxy_list = while_list
        while_list = []
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Getting new proxy . . .')
        proxy_list = while_list.copy()
        proxy_list.extend(getProxy())
        while_list = []
        os.system('cls' if os.name == 'nt' else 'clear')