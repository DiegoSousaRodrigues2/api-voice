import http
from flask import Flask, jsonify, request
import driveService
import voiceService

app = Flask(__name__)


@app.route('/')
def test_autorization():
    response = driveService.check_token()
    if response != "OK":
        return jsonify({'Message': 'Api working', 'Status': http.HTTPStatus.OK})
    else:
        return jsonify({'Message': response, 'Status': http.HTTPStatus.BAD_REQUEST})


@app.route('/listAudios')
def list_audios_from_google_drive():
    return driveService.list_file()


@app.route('/download')
def download_audio_and_change_to_text():
    args = request.args
    file_id = args.get('id')
    file_name = args.get('name')
    if file_id is None or file_name is None:
        return jsonify({'Message': 'Inconsistencia no parametro', 'Status': http.HTTPStatus.BAD_REQUEST})
    status = driveService.download_file(file_id, file_name)
    if status == "Error":
        return jsonify({'Message': 'Error', 'Status': http.HTTPStatus.BAD_REQUEST})
    message = voiceService.speeach_to_texto("audios/" + file_name)
    return jsonify({'Message': message, 'Status': http.HTTPStatus.OK})


@app.route('/getAudioById')
def get_audio_by_id():
    args = request.args
    file_id = args.get('id')
    if file_id is None:
        return jsonify({'Message': 'Inconsistencia no parametro', 'Status': http.HTTPStatus.BAD_REQUEST})
    audio = driveService.get_file(file_id)
    if audio is not None:
        return jsonify(audio)
    else:
        return jsonify({'Message': 'Arquivo não encontrado', 'Status': http.HTTPStatus.NOT_FOUND})


app.run(host='0.0.0.0')
