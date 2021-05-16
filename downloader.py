import bs4 as bs
import urllib.request
from pytube import YouTube
import os, platform
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import moviepy.editor as mp

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


''' Function to take input Initial Message '''
def response():
    if platform.system() =='Windows':
        os.system("cls")
    else:
        os.system("clear")
    print("WELCOME TO THE YOUTUBE PLAYLIST DOWNLOADER")
    print("Choose a downloading mode : \n 1. Single video \n 2. Playlist \n 3. Video to Audio Convertor \n")
    mode = int(input())
    if mode==3:
        return mode
    else:
        url = input("Please paste the playlist or video link : ")
        return url, mode

''' Function to print final message '''
def thanks():
    if platform.system() =='Windows':
        os.system("cls")
    else:
        os.system("clear")
    time.sleep(3)


''' Function to scrap the youtube for playlist link '''
def linkscrapper(url_link):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    driver.get(url_link)
    page = driver.page_source
    driver.quit()
    scrap = bs.BeautifulSoup(page, 'lxml')
    #print(scrap)
    videos = scrap.find_all("a", class_="yt-simple-endpoint style-scope ytd-playlist-panel-video-renderer")
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
    createFolder("Downloads")
    for i in video_list:
        video_count += 1
        yt = YouTube(i)
        stream = yt.streams.first()
        print("Downloading video(" + str(video_count) + "/" + str(length) + ")" + "(" + str(math.ceil(stream.filesize/(1024*1024))) + "MB)")
        video_extension = stream.mime_type.split('/')        
        #stream.download("Downloads/")
        file_name = yt.title + "." + video_extension[1]
        if os.path.exists(file_name):
            print("File Exists")
        else:
            stream.download("Downloads/")

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
        stream.download("Downloads/")

def audio():
    video_file = input("Please paste the path of video : ")
    out_file = input()
    my_clip = mp.VideoFileClip(video_file)
    my_clip.audio.write_audiofile(out_file+".mp3")

if __name__ =="__main__":
    inp = response()
    #print(type(inp[1]))
    if inp == 3:
        audio()
    elif inp[1] == 1: 
        single_video(inp[0])
    elif inp[1] == 2:
        playlist(inp[0])
    thanks()
