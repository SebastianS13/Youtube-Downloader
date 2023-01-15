from pytube import YouTube
from sys import argv

link = input("Video link: ")
path = input("Where should it be saved: ")
yt = YouTube(link)

print("Downloading: ", yt.title)

yd = yt.streams.get_highest_resolution()
yd.download(path)