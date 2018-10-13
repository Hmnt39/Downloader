import bs4 as bs
import urllib.request
from pytube import YouTube
import os
import time
import math


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def response():
    os.system("cls")
    print("WELCOME TO THE WEBCANVA YOUTUBE PLAYLIST DOWNLOADER \n Created by Webcanva (webcanva.com)")
    time.sleep(2)
    url = input("Please paste the playlist link : ")
    return url


def thanks():
    os.system("cls")
    print("Thanks for using our software. If you have any suggestions please mail us \n (design.webcanva@gmail.com)" +
          "\n Hemant Kumar Mishra")
    time.sleep(3)


def playlist(url_link):
    url = urllib.request.urlopen(url_link)
    scrap = bs.BeautifulSoup(url, 'lxml')
    videos = scrap.find_all("a", class_=" spf-link playlist-video clearfix yt-uix-sessionlink spf-link ")
    print(len(videos), " Videos found")
    video_link = []
    link = "https://www.youtube.com"
    for j in videos:
        video_link.append(link+j['href'])
    return video_link


def download():
    url = response()
##    directory = input("Type the folder name :")
##    createFolder(directory)
##    os.chdir(directory)
    video_list = playlist(url)
    video_count = 0
    length = len(video_list)
    for i in video_list:
        video_count += 1
        yt = YouTube(i)
        stream = yt.streams.first()
        print("Downloading " + yt.title + "(" + str(math.ceil(stream.filesize/(1024*1024))) + "MB)")
        video_extension = stream.mime_type.split('/')
        file_name = yt.title + "." + video_extension[1]
        if os.path.exists(file_name):
            print("File Exists")
        else:
            stream.download()
            print("Downloaded (" + str(video_count) + "/" + str(length) + ")")
    thanks()


download()
