import http
from flask import Flask, jsonify, request

import driveService

app = Flask(__name__)


@app.route('/')
def test_autorization():
    status = driveService.check_token()
    if status == "OK":
        return jsonify({'Message': 'Api working', 'Status': http.HTTPStatus.OK})


@app.route('/listAudios')
def list_audios_from_google_drive():
    return jsonify(driveService.connect_and_get_list_of_itens())


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
    file_id = '1h1Lm6SOvwo50kWoRw9PiSzJMWjjajdMW'
    _, creds = driveService.check_token()
    driveService.FileDownload(creds, file_id)
    return "OK"

app.run(host='0.0.0.0')
