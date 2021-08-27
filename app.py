#!/usr/bin/python3
from flask import Flask, render_template, url_for
from re import findall
import os
from subprocess import call
from config import STREAM_ADDRESS, VIDEO_DIRECTORY, APP_DIRECTORY, FLASK_HOST, PORT

# change direcotory in order to get video size

app = Flask(__name__, static_folder=VIDEO_DIRECTORY)

def getFiles():
    os.chdir(VIDEO_DIRECTORY)
    dic = {}
    files = os.listdir()
    if len(files):
        files.sort(key=os.path.getctime)
        for i in files:
            if i == 'lastsnap.jpg':
                continue

            urlFor = url_for('static', filename=i)

            # dafault motion filename 0-01-20210827124404.mkv
            date = findall('[0-9]{14}', i)[0] # 20210827124404
            day = date[:4] + '/' + date[4:6] + '/' + date[6:8]
            time_ = date[8:10] + ':' + date[10:12] + ':' + date[12:]

            size = os.path.getsize(i)
            end = 'B'
            for j in range(4):
                if size > 1000:
                    size /= 1000
                    end = ['K','M','G','T'][j]
                else:
                    break
            size = f'{round(size, 1)}{end}'

            if day not in dic.keys():
                dic[day] = {}

            dic[day][time_] = [urlFor, size]
    os.chdir(APP_DIRECTORY)
    return dic

@app.route('/')
def index():
    files = getFiles()
    return render_template('index.html', address=STREAM_ADDRESS, files=files)

@app.route('/delete/<video>')
def delete(video):
    print('Deleting ' + video)
    call('sudo rm ' + os.path.join(VIDEO_DIRECTORY, video), shell=True)
    return 'deleted'

if __name__ == '__main__':
    try:
        app.run(FLASK_HOST, PORT)
    except Exception as e:
        print(e)