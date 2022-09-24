from pytube import YouTube
import os

PATH = 'download'

url = "A/url/Aqui"

yt = YouTube(url)
audio = yt.streams.filter(only_audio=True)[0]
audio.download(PATH+'/')

os.rename(PATH+'/'+audio.default_filename, PATH+'/'+audio.default_filename+'.mp3')