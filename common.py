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

_SOCKET = socket.socket

def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)


def getProxy(protocol='http', timeout=700):
    try:
        socket.socket = _SOCKET
        req = urllib.request.Request(
            f'https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol}&timeout={timeout}&country=all&ssl=all&anonymity=all')
        response = urllib.request.urlopen(req)
        proxy_list_str = response.read().decode('utf-8')
        proxy_list = proxy_list_str.split('\r\n')
        random.shuffle(proxy_list)
        return proxy_list
    except Exception:
        return []


def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)


def getSockType(protocol):
    if(protocol == 'http'):
        return socks.HTTP
    elif(protocol == 'socks4'):
        return socks.SOCKS4
    elif(protocol == 'socks5'):
        return socks.SOCKS5
    return socks.HTTP


def log(status_code, protocol, referrer):
    if(status_code == 200):
        os.system('cls' if os.name == 'nt' else 'clear')  # clear man hinh
        with open("temp.txt", "a") as f:
            f.write("1")
        with open("temp.txt", "r") as f:
            t = f.read()
            print(f'{len(t)}')
    # else:
    #     common.bad += 1
    # os.system('cls' if os.name == 'nt' else 'clear')  # clear man hinh
    # # print(f"Boots warp+ ip {referrer} using {protocol}")
    # print(f"Good: {common.good}")
    # print(f"Bad : {common.bad}")
    # print(f'Total request: {common.good + common.bad}')


class WrapPlus:
    def __init__(self, protocol, timeout,referrer="0a104a80-c6c1-4ea0-ac2d-f72b664b6aed"):
        self._PROTOCOL = protocol
        self._SOCK_TYPE = getSockType(str.lower(protocol))
        self._TIMEOUT = timeout
        self._REFERRER = referrer
        self.time_start = dt.timestamp(dt.now())

    def boost(self, proxy_host='', t=0):
        try:
            url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
            install_id = genString(22)
            headers = {'Content-Type': 'application/json; charset=UTF-8',
                       'Host': 'api.cloudflareclient.com',
                       'Connection': 'Keep-Alive',
                       'Accept-Encoding': 'gzip',
                       'User-Agent': 'okhttp/3.12.1'
                       }
            body = {"key": "{}=".format(genString(43)),
                    "install_id": install_id,
                    "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                    "referrer": self._REFERRER,
                    "warp_enabled": False,
                    "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                    "type": "Android",
                    "locale": "es_ES"}
            data = json.dumps(body).encode('utf8')
            if(proxy_host != "" and t == 0):
                pro = proxy_host.split(':')
                socks.set_default_proxy(self._SOCK_TYPE, pro[0], int(pro[1]))
                socket.socket = socks.socksocket
            elif proxy_host == "" and t == 0:
                socket.socket = _SOCKET
            req = urllib.request.Request(url, data, headers)
            if t > 0:
                response = urllib.request.urlopen(req, timeout=10)
            else:
                response = urllib.request.urlopen(req, timeout=3)
            status_code = response.getcode()
            return status_code
        except Exception:
            return 500

    def doBoost(self, proxy_list):
        while_list = []
        for proxy in proxy_list:
            for i in range(3):
                result = self.boost(proxy, i)
                log(result, self._PROTOCOL, self._REFERRER)
                if result == 200:
                    if i == 0:
                        while_list.append(proxy)
                else:
                    break
            if dt.timestamp(dt.now()) - self.time_start > 18:
                result = self.boost()
                self.time_start = dt.timestamp(dt.now())
            if len(while_list) > 9:
                while_list = self.doBoost(while_list)
        return while_list

    def run(self):
        proxy_list = []
        while True:
            next_proxy_list = getProxy(
                self._PROTOCOL, self._TIMEOUT)             # new proxies
            proxy_list.extend(next_proxy_list)
            while_list = self.doBoost(proxy_list)
            proxy_list = while_list.copy()
##################################################################################
