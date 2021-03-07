import os
import signal
import subprocess
# import psutil
# from pynput.keyboard import Listener
# times = input('Nhập số luồn cho cả 3 loại proxy')
times = 3
files = [
    'via-http.py',
    'via-socks4.py',
    'via-http.py',
    'via-socks4.py',
    'via-socks5.py'
]
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
process_id_list = []
for i in range(int(times)):
    for filei in files:
        pass
        process_id_list.append(subprocess.Popen(
            [f'{CURR_DIR}\\warp-\\{filei}'], shell=True))
