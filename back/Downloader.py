from pytube import YouTube

from pytube.exceptions import RegexMatchError
from pytube.exceptions import VideoPrivate
from pytube.exceptions import ExtractError
from pytube.exceptions import VideoUnavailable

from os import rename
from datetime import datetime


class Downloader:
    PATH = 'download/'
    NAME_FOLER = ''

    def __init__(self):
        pass

    def get_group_folder(self):
        """ Método para obter a data atual e utilizá-la para agrupar os downloads
        """
        data_hoje = datetime.now()
        self.NAME_FOLER = data_hoje.strftime('%Y-%m-%d') + '/'


    def get_audio_mp3(self, url: str) -> None:
        """ Método para realizar o download do aúdio do vídeo na url passada
        
        Parameters:
            url (str): O endereço do vídeo no youtube.
        """
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True)[0] # Esse [0] deve ser a qualidade
        self.get_group_folder()
        path_to_download = self.PATH + self.NAME_FOLER
        audio.download(path_to_download)
        rename(path_to_download + audio.default_filename, path_to_download + audio.default_filename.replace('.mp4','.mp3'))



    def get_video_mp4(self, url):
        """ Método para realizar o download do vídeo do vídeo na url passada
        
        Parameters:
            url (str): O endereço do vídeo no youtube.
        """

        yt = YouTube(url)
        video = yt.streams.filter()[0] # Esse [0] deve ser a qualidade
        self.get_group_folder()
        path_to_download = self.PATH + self.NAME_FOLER
        video.download(path_to_download)
        #os.rename(self.PATH + video.default_filename)
       