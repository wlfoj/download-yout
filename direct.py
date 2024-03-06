from pytube import YouTube
import os

PATH = 'download'

url = "https://www.youtube.com/watch?v=Qdskk_oJdbY&ab_channel=BonJovi-Topic"

yt = YouTube(url)
audio = yt.streams.filter(only_audio=True)[0]
audio.download(PATH+'/')

os.rename(PATH+'/'+audio.default_filename, PATH+'/'+audio.default_filename.replace('.mp4','')+'.mp3')
