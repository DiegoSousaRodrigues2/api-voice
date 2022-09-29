import time

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
    print(res.json()['id'])
    return res.json()['id']


def verify_id(job_id):
    response = None
    do_while = True
    while do_while:
        endpoint = "https://sandbox.zamzar.com/v1/jobs/{}".format(job_id)
        response = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
        print(response.json())
        try:
            print(response.json()['target_files'][0]['id'])
            do_while = False
        except:
            time.sleep(0.3)
    return response.json()['target_files'][0]['id']


def download(file_id, file_name):
    local_file_name = './audios/' + str(file_name).replace(str(file_name)[-4::], '.wav')
    endpoint = "https://sandbox.zamzar.com/v1/files/{}/content".format(file_id)

    response = requests.get(endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))

    try:
        with open(local_file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

            print("File downloaded")

    except IOError:
        print("Error")
    return local_file_name


def route(file_name):
    job_id = upload_and_conversion('audios/' + file_name)
    #job_id = 30066680
    time.sleep(1)  # Sleep to convert de audio at time
    file_id = verify_id(job_id)
    return download(file_id, file_name)
