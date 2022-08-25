import http
from flask import Flask, jsonify, request

import connect

app = Flask(__name__)


@app.route('/')
def test_autorization():
    return jsonify({'Message': 'Api working', 'Status': http.HTTPStatus.OK})


@app.route('/listAudios')
def list_audios_from_google_drive():
    return jsonify(connect.connect_and_get_list_of_itens())


@app.route('/getAudio')
def get_audio_from_google_drive():
    args = request.args
    id = args.get('id')
    audio = connect.connect_and_get_list_of_itens()
    if audio.get(id):
        return jsonify({'id': audio.get(id)})
    else:
        return jsonify({'Message': 'Arquivo não encontrado', 'Status': http.HTTPStatus.NOT_FOUND})


app.run(host='0.0.0.0')
