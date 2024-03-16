from flask import Flask, request, jsonify

import json

import logging

from flasgger import Swagger

from Downloader import Downloader

from pytube.exceptions import RegexMatchError
from pytube.exceptions import VideoPrivate
from pytube.exceptions import ExtractError
from pytube.exceptions import VideoUnavailable


# ===== Configuração do logg ===== #
logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(asctime)s] [%(levelname)s] [%(module)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %zH %p',
                    filename='back/logs.log', encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)
prefix = "/api/V1/"
swagger = Swagger(app)
downloader = Downloader()


# ========== Definição das Rotas ========== #
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
    logger.info('Verificou-se o status da aplicação')
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
    logger.info('Recebido solicitação de download para mp3 no link %s ', url)
    # Fazer o captador de exceção aqui
    try:
        downloader.get_audio_mp3(url)
        logger.info('Solicitação de download para mp3 no link %s foi atendida com sucesso', url)
        res = {'message': 'audio downloaded'}
        return jsonify(res), 201
    except RegexMatchError as err:
        logger.exception('Download interrompido. A exceção foi lançada. ' + err)
        return jsonify({'error': 'Link inválido'}), 400
    except VideoUnavailable as err:
        logger.exception('Download interrompido. A exceção foi lançada. ' + err)
        return jsonify({'error': 'Vídeo não disponível para download'}), 404
    except VideoPrivate as err:
        logger.exception('Download interrompido. A exceção foi lançada. ' + err)
        return jsonify({'error': 'Vídeo não encontrado'}), 404
    except Exception as err: #??????
        logger.error('Download interrompido. A exceção foi lançada. ' + err)
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
    logger.info('Recebido solicitação de download para mp4 no link %s ', url)
    # Fazer o captador de exceção aqui
    try:
        downloader.get_video_mp4(url)
        res = {'message': 'video downloaded'}
        logger.info('Solicitação de download para mp3 no link %s foi atendida com sucesso', url)
        return jsonify(res), 201
    except RegexMatchError as err:
        logger.exception('Download interrompido. A exceção foi lançada. ' + err)
        return jsonify({'error': 'Link inválido'}), 400
    except VideoUnavailable as err:
        logger.exception('Download interrompido. A exceção foi lançada. ' + err)
        return jsonify({'error': 'Vídeo não disponível para download'}), 404
    except VideoPrivate as err:
        logger.exception('Download interrompido. A exceção foi lançada. ' + err)
        return jsonify({'error': 'Vídeo não encontrado'}), 404
    except Exception as err: #??????
        logger.error('Download interrompido. A exceção foi lançada. ' + err)
        return jsonify({'error': 'Vídeo não encontrado'}), 500





if __name__ == '__main__':
    app.run(debug=True)