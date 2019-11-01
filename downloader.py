import bs4 as bs
import urllib.request
from pytube import YouTube
import os, platform
import time
import math

'''

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
'''

''' Function to take input Initial Message '''
def response():
    if platform.system() =='Windows':
        os.system("cls")
    else:
        os.system("clear")
    print("WELCOME TO THE YOUTUBE PLAYLIST DOWNLOADER")
    time.sleep(2)
    print("Choose a downloading mode : \n 1. Single video \n 2. Playlist \n")
    mode = int(input())
    url = input("Please paste the playlist or video link : ")
    return url, mode

''' Function to print final message '''
def thanks():
    if platform.system() =='Windows':
        os.system("cls")
    else:
        os.system("clear")
    print("Thanks for using our software" +
          "\n Hemant Kumar Mishra")
    time.sleep(3)


''' Function to scrap the youtube for playlist link '''
def linkscrapper(url_link):
    url = urllib.request.urlopen(url_link)
    scrap = bs.BeautifulSoup(url, 'lxml')
    videos = scrap.find_all("a", class_="spf-link playlist-video clearfix yt-uix-sessionlink spf-link")
    print(len(videos), " Videos found")
    video_link = []
    link = "https://www.youtube.com"
    for j in videos:
        video_link.append(link+j['href'])
    return video_link


'''Function to download playlist '''
def playlist(url):
    video_list = linkscrapper(url)
    video_count = 0
    length = len(video_list)
    for i in video_list:
        video_count += 1
        yt = YouTube(i)
        stream = yt.streams.first()
        print("Downloading video(" + str(video_count) + "/" + str(length) + ")" + "(" + str(math.ceil(stream.filesize/(1024*1024))) + "MB)")
        video_extension = stream.mime_type.split('/')        
        stream.download()
        '''  To check if file exists
        file_name = yt.title + "." + video_extension[1]
        if os.path.exists(file_name):
            print("File Exists")
        else:
            stream.download()
        '''

''' Function to download single video '''
def single_video(url):
    yt = YouTube(url)
    stream = yt.streams.first()
    print("Downloading video" + "(" + str(math.ceil(stream.filesize/(1024*1024))) + "MB)")
    video_extension = stream.mime_type.split('/')
    file_name =  "output." + video_extension[1]
    if os.path.exists(file_name):
        print("File Exists")
    else:
        stream.download()
        print(" Video Downloaded ")

if __name__ =="__main__":
    url, mode = response()
    if mode == 1: 
        single_video(url)
    if mode == 2:
        playlist(url)
    thanks()
