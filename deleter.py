import subprocess, datetime
from os import listdir
from config import VIDEO_EXTENSION

now = datetime.datetime.now()
lastday = now - datetime.timedelta(days=3)

filename = lastday.strftime('%Y%m')

files = listdir('/var/lib/motion/')
filess = set([i[3:-10] for i in files if i.endswith(VIDEO_EXTENSION)])
files_to_remove = [file for file in filess if file not in [f'{filename}{day}' for day in range(lastday.day, now.day+1)]]
while '' in files_to_remove:
    files_to_remove.remove('')

for i in sorted(files_to_remove):
    command = 'sudo rm /var/lib/motion/*' + i + '*'
    print(command)
    subprocess.call(command, shell=True)