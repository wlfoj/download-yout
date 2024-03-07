from flask import Flask, request, jsonify

import json

from flasgger import Swagger

from pytube.exceptions import RegexMatchError
from pytube.exceptions import VideoPrivate
from pytube.exceptions import ExtractError
from pytube.exceptions import VideoUnavailable

from Downloader import Downloader

app = Flask(__name__)

swagger = Swagger(app)

downloader = Downloader()

prefix = "/api/V1/"


@app.route(prefix + '<string:name>/', methods=['GET'])
def Hello(name):
    """
    Apresenta o status da API.

    ---
    responses:
      200:
        description: API operando normalmente.
      500:
        description: API com problemas??.
    """
    res = {'message': 'Olá ' + name +', estamos funcionando normalmente'}
    return jsonify(res), 200



@app.route(prefix + "mp3/", methods=['POST'])
def Download_MP3():
    """
    Baixa o áudio de um vídeo no YT a partir da URL fornecida.

    Ao realizar o download do áudio, põe o mesmo na pasta 'download' dentro da pasta cujo nome é a data do dia do download do áudio.
    Ao baixar o áudio de uma música com o nome 'Dilion.mp3' em 01/26/2024, a visão do arquivo será esta:
    Exemplo:
    
    | download/
    |___ 2024-01-26/
    |_____ Dilion.mp3

    ---
    parameters:
      - name: url
        in: formData
        type: string
        required: true
        description: A URL do vídeo.
    responses:
      201:
        description: O áudio mp3 foi baixado com sucesso.
      400:
        description: A URL fornecida não é um link de vídeo válido.
      500:
        description: Houve um problema interno ao processar a solicitação.
    """
    dados = json.loads(request.data)
    url = dados['url']

    # Fazer o captador de exceção aqui
    try:
        downloader.get_audio_mp3(url)
        res = {'message': 'baixa mp3'}
        return jsonify(res), 201
    except RegexMatchError:
        return jsonify({'error': 'Link inválido'}), 400
    except VideoUnavailable:
        return jsonify({'error': 'Vídeo não disponível para download'}), 404
    except VideoPrivate:
        return jsonify({'error': 'Vídeo não encontrado'}), 404
    except Exception: #??????
        return jsonify({'error': 'Vídeo não encontrado'}), 500
    



@app.route(prefix + "mp4/", methods=['POST'])
def Download_MP4():
    """
    Baixa o video do YT a partir da URL fornecida.

    Ao realizar o download do video, põe o mesmo na pasta 'download' dentro da pasta cujo nome é a data do dia do download do video.
    Ao baixar o video de clip musical com o nome 'Dilion.mp4' em 01/26/2024, a visão do arquivo será esta:
    Exemplo:
    
    | download/
    |___ 2024-01-26/
    |_____ Dilion.mp4
    ---
    parameters:
      - name: url
        in: formData
        type: string
        required: true
        description: A URL do vídeo.
    responses:
      201:
        description: O video mp4 foi baixado com sucesso.
      400:
        description: A URL fornecida não é um link de vídeo válido.
      500:
        description: Houve um problema interno ao processar a solicitação.
    """
    dados = json.loads(request.data)
    url = dados['url']

    # Fazer o captador de exceção aqui
    try:
        downloader.get_video_mp4(url)
        res = {'message': 'baixa mp4'}
        return jsonify(res), 201
    except RegexMatchError:
        return jsonify({'error': 'Link inválido'}), 400
    except VideoUnavailable:
        return jsonify({'error': 'Vídeo não disponível para download'}), 404
    except VideoPrivate:
        return jsonify({'error': 'Vídeo não encontrado'}), 404
    except Exception: #??????
        return jsonify({'error': 'Vídeo não encontrado'}), 500





if __name__ == '__main__':
    app.run(debug=True)