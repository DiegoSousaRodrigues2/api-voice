from __future__ import print_function
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path

CLIENTE_SECRETE_FILE = 'token.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive']


def check_token():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES[0])
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


def FileDownload(cred, file_id):
    try:
        service = build(API_NAME, API_VERSION, credentials=cred)
        print(API_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

# Initialise a downloader object to download the file
# downloader = MediaIoBaseDownload(fh, request, chunksize=204800)
# done = False

# try:
#     # Download the data in chunks
#     while not done:
#         status, done = downloader.next_chunk()
#
#     fh.seek(0)
#
#     # Write the received data to the file
#     with open(file_name, 'wb') as f:
#         shutil.copyfileobj(fh, f)
#
#     print("File Downloaded")
#     return True
# except:
#     # Return False if something went wrong
#     print("Something went wrong.")
#     return False


# def FileUpload(self, filepath):
#     # Extract the file name out of the file path
#     name = filepath.split('/')[-1]
#
#     # Find the MimeType of the file
#     mimetype = MimeTypes().guess_type(name)[0]
#
#     # create file metadata
#     file_metadata = {'name': name}
#
#     try:
#         media = MediaFileUpload(filepath, mimetype=mimetype)
#
#         # Create a new file in the Drive storage
#         file = self.service.files().create(
#             body=file_metadata, media_body=media, fields='id').execute()
#
#         print("File Uploaded.")
#
#     except:
#
#         # Raise UploadError if file is not uploaded.
#         raise print("Can't Upload File.")
#

if __name__ == "__main__":
    i = int(input("Enter your choice:1 - Download file, 2- Upload File, 3- Exit.\n"))

    if i == 1:
        f_id = input("Enter file id: ")
        f_name = input("Enter file name: ")
        FileDownload(f_id, f_name)

    elif i == 2:
        f_path = input("Enter full file path: ")
        FileUpload(f_path)

    else:
        exit()
