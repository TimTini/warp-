import os
import time
import signal
import subprocess
import psutil
from pynput.keyboard import Listener
# times = input('Nhập số luồn cho cả 3 loại proxy')
times = 4
files = [
    'via-http.py',
    'via-socks4.py',
    'via-http.py',
    'via-socks4.py',
    'via-socks5.py'
]
process_id_list = []
for i in range(int(times)):
    for filei in files:
        process_id_list.append(subprocess.Popen([f'{filei}'], shell=True))
count_key = 0


def anonymous(key):
    global count_key
    key = str(key)
    print(key)
    if key == 'Key.esc':
        count_key += 1
        print(count_key)
        if count_key > 10:
            for shell_process in process_id_list:
                parent = psutil.Process(shell_process.pid)
                children = parent.children(recursive=True)
                child_pid = children[0].pid
                print("Taskkill /PID %d /F" % child_pid)
                subprocess.check_output("Taskkill /PID %d /F" % child_pid)
            exit()
    else:
        count_key = 0


with Listener(on_press=anonymous) as listener:
    listener.join()
