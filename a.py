import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENTE_SECRET_FILE = 'client_secret_821515524601-k84jba25uosbk2187otohim5k6ime0li.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENTE_SECRET_FILE, API_NAME, API_VERSION, SCOPE)

file_ids = ['1h1Lm6SOvwo50kWoRw9PiSzJMWjjajdMW', '1YaTelpi26kO32M0LpUSwAEXFRu17Lj7Q']
file_names = ['integrantes.txt', 'Coordenadas da escadona.txt']

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False

    while not done:
        status, done = downloader.next_chunk()
        print('Donwload progress {0}'.format(status.progress() * 100))

    fh.seek(0)
    with open(os.path.join('./teste', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
