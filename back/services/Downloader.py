from pytube import YouTube

from pytube.exceptions import RegexMatchError
from pytube.exceptions import VideoPrivate
from pytube.exceptions import ExtractError
from pytube.exceptions import VideoUnavailable

from datetime import datetime

import logging

class Downloader:
    PATH = 'download/'
    NAME_FOLER = ''

    def __init__(self):
        self.logger = logging.getLogger(__name__)


    def get_group_folder(self):
        """ Método para obter a data atual e utilizá-la para agrupar os downloads
        """
        data_hoje = datetime.now()
        self.NAME_FOLER = data_hoje.strftime('%Y-%m-%d') + '/'


    def get_audio_mp3(self, url: str) -> None:
        """ Método para realizar o download do aúdio do vídeo na url do parâmetro
        
        Parameters:
            url (str): O endereço do vídeo no youtube.
        """
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True)[0]
        self.get_group_folder()
        path_to_download = self.PATH + self.NAME_FOLER
        self.logger.info("Iniciando Download de '%s'  '%s' %sMb", audio.default_filename, audio.title, audio.filesize_mb)
        audio.download(output_path=path_to_download, filename=audio.default_filename.replace('.mp4','.mp3'))
        self.logger.info("Download concluído e salvo em '%s%s'", path_to_download, audio.default_filename.replace('.mp4','.mp3'))



    def get_video_mp4(self, url):
        """ Método para realizar o download do vídeo do vídeo na url do parâmetro
        
        Parameters:
            url (str): O endereço do vídeo no youtube.
        """

        yt = YouTube(url)
        video = yt.streams.filter()[0]
        self.get_group_folder()
        path_to_download = self.PATH + self.NAME_FOLER
        self.logger.info("Iniciando Download de '%s'  '%s' %sMb", video.default_filename, video.title, video.filesize_mb)
        video.download(path_to_download)
        self.logger.info("Download concluído e salvo em '%s%s'", path_to_download, video.default_filename)
       