from __future__ import print_function
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Imports para download dos arquivos do Google drive
import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENTE_SECRETE_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
SCOPES_AUTENTICATION = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def check_token():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES_AUTENTICATION)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return "OK", creds


def download_file(file_id, file_name):
    CLIENTE_SECRET_FILE = 'client_secret_821515524601-k84jba25uosbk2187otohim5k6ime0li.apps.googleusercontent.com.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPE = ['https://www.googleapis.com/auth/drive']
    service = Create_Service(CLIENTE_SECRET_FILE, API_NAME, API_VERSION, SCOPE)
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
