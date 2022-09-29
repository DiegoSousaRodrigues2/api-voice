import http
from flask import Flask, jsonify, request
import DriveService
import VoiceController
import VoiceService
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


@app.route('/health/drive')
def test_autorization_google_drive_api():
    response = DriveService.check_token()
    if response != "OK":
        return jsonify({'Message': 'Api working', 'Status': http.HTTPStatus.OK})
    else:
        return jsonify({'Message': response, 'Status': http.HTTPStatus.BAD_REQUEST})


@app.route('/health/zamzar')
def teste_autorization_zamzar_api():
    api_key = '8f6ea174098cb43316cd3c7779067747519f58b9'
    endpoint = "https://sandbox.zamzar.com/v1/formats/gif"
    requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
    return jsonify({'Message': 'Api working', 'Status': http.HTTPStatus.OK})


@app.route('/listAudios')
def list_audios_from_google_drive():
    return DriveService.list_file()


@app.route('/download')
def download_audio_and_change_to_text():
    args = request.args
    file_id = args.get('id')
    file_name = args.get('name')
    if file_id is None or file_name is None:
        return jsonify({'Message': 'Inconsistencia no parametro', 'Status': http.HTTPStatus.BAD_REQUEST})
    status = DriveService.download_file(file_id, file_name)
    if status == "Error":
        return jsonify({'Message': 'Error', 'Status': http.HTTPStatus.BAD_REQUEST})
    star, message = VoiceController.route(file_name)
    return jsonify({'Message': message, 'Star': star, 'Status': http.HTTPStatus.OK})


@app.route('/getAudioById')
def get_audio_by_id():
    args = request.args
    file_id = args.get('id')
    if file_id is None:
        return jsonify({'Message': 'Inconsistencia no parametro', 'Status': http.HTTPStatus.BAD_REQUEST})
    audio = DriveService.get_file(file_id)
    if audio is not None:
        return jsonify(audio)
    else:
        return jsonify({'Message': 'Arquivo não encontrado', 'Status': http.HTTPStatus.NOT_FOUND})


app.run(host='0.0.0.0')
