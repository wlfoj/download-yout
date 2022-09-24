from pytube import YouTube
import os

PATH = 'download'
URL = "https://www.youtube.com/watch?v=mWQACEqf4QY"
yt = YouTube(URL)
audio = yt.streams.filter(only_audio=True)[0]
audio.download(PATH+'/')
os.rename(PATH+'/'+audio.default_filename, PATH+'/'+audio.default_filename+'.mp3')