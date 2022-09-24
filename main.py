from pytube import YouTube
from pytube.exceptions import RegexMatchError
from pytube.exceptions import VideoPrivate
from pytube.exceptions import ExtractError
from pytube.exceptions import VideoUnavailable

import os

PATH = 'download'

def clean_screen():
    """Procedimento para limpar a tela"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")


def menu():
    """Função que mantém o usuário no processo até que o mesmo decida sair"""
    continuar = 's'.lower()
    while continuar == 's':
        clean_screen()
        main()
        continuar = input("Digite S para continuar e qualquer outra tecla para sair: ").lower()


def main():
    err = False # Não é mais necessário
    url = input('Digite o link do video: ')
    while True:
        try:
            option = input('Digite [1] para baixar áudio/ [2] para baixar o vídeo:  ')
            option = int(option)
            if option != 1 and option != 2:
                raise Exception
            err = False
            break
        except:
            print('Digite uma opção válida')
            err = True

    if (not err and option == 1):
        download_audio(url)
    elif(not err and option ==2):
        download_video(url)

#https://www.youtube.com/watch?v=q_oy97fTn3w
def download_audio(url: str):
    '''Procedimento para baixar apenas o audio'''
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True)[0]
        audio.download(PATH+'/')
        os.rename(PATH+'/'+audio.default_filename, PATH+'/'+audio.default_filename+'.mp3')
        print(f"O download de '{audio.title}' concluído com sucesso!!")
    except RegexMatchError:
        print('Link com problemas, verifique se está correto')
    except VideoPrivate:
        print("Este video está privado")
    except ExtractError:
        print("Erro na extração do video")
    except VideoUnavailable:
        print("O video está indisponivel")


def download_video(url: str):
    '''Procedimento para baixar video com audio'''
    try:
        yt = YouTube(url)
        video = yt.streams.filter(file_extension='mp4')[0]
        video.download(PATH+'/')
        print(f"O download de '{video.title}' concluído com sucesso!!")
    except RegexMatchError:
        print('Link com problemas, verifique se está correto')
    except VideoPrivate:
        print("Este video está privado")
    except ExtractError:
        print("Erro na extração do video")
    except VideoUnavailable:
        print("O video está indisponivel")


if __name__ == "__main__":
    menu()

# Adicionar opção de escolher a resolução
# Melhorar a parte das exceções para não ter código repetido