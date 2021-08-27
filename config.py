from socket import socket, AF_INET, SOCK_DGRAM
from os import system
from sys import path

FLASK_HOST = '0.0.0.0'
PORT = 8000
VIDEO_DIRECTORY = '/var/lib/motion'
APP_DIRECTORY = path[0]
VIDEO_EXTENSION = 'mkv'

# If you have a static ip or stream address you can remove this part
# wait for internet connection before getting local ip
response = system("ping -c 1 google.com")
while response != 0:
    response = system("ping -c 1 google.com")

def getLocalIp():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

STREAM_ADDRESS = f'http://{getLocalIp()}:8081'