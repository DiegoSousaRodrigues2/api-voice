from __future__ import print_function
# Imports para download dos arquivos do Google drive
import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENTE_SECRET_FILE = 'env/client_secret_821515524601-k84jba25uosbk2187otohim5k6ime0li.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']


def check_token():
    try:
        Create_Service(CLIENTE_SECRET_FILE, API_NAME, API_VERSION, SCOPE)
        return "Ok"
    except Exception as e:
        return e


def download_file(file_id, file_name):
    service = Create_Service(CLIENTE_SECRET_FILE, API_NAME, API_VERSION, SCOPE)
    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False

    while not done:
        status, done = downloader.next_chunk()
        print('Donwload progress {0}'.format(status.progress() * 100))

    fh.seek(0)
    with open(os.path.join('audios', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
