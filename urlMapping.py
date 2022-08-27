import http
from flask import Flask, jsonify, request

import driveService

app = Flask(__name__)


@app.route('/')
def test_autorization():
    status, _ = driveService.check_token()
    if status == "OK":
        return jsonify({'Message': 'Api working', 'Status': http.HTTPStatus.OK})


@app.route('/listAudios')
def list_audios_from_google_drive():
    return jsonify(driveService.list())


@app.route('/getAudio')
def get_audio_from_google_drive():
    args = request.args
    id = args.get('id')
    audio = driveService.connect_and_get_list_of_itens()
    if audio.get(id):
        return jsonify({'id': audio.get(id)})
    else:
        return jsonify({'Message': 'Arquivo não encontrado', 'Status': http.HTTPStatus.NOT_FOUND})


@app.route('/download')
def download_audio():
    file_id = '1ite8-HbIAu8coaGqeBr2OC4MYBbOaRUu'
    file_name = 'teste.mp3'
    driveService.download_file(file_id, file_name)
    return "OK"


app.run(host='0.0.0.0')
