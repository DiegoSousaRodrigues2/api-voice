import requests
from requests.auth import HTTPBasicAuth

api_key = '8f6ea174098cb43316cd3c7779067747519f58b9'


def upload_and_conversion(path):
    endpoint = "https://sandbox.zamzar.com/v1/jobs"
    source_file = path
    target_format = "wav"

    file_content = {'source_file': open(source_file, 'rb')}
    data_content = {'target_format': target_format}
    res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
    print(res.json())


def verify_id():
    job_id = 30009574
    endpoint = "https://sandbox.zamzar.com/v1/jobs/{}".format(job_id)

    response = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))

    print(response.json())


def download():
    file_id = 134588976
    local_filename = './audios/a3.wav'
    endpoint = "https://sandbox.zamzar.com/v1/files/{}/content".format(file_id)

    response = requests.get(endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))

    try:
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

            print("File downloaded")

    except IOError:
        print("Error")


def route(path):
    upload_and_conversion(path)
