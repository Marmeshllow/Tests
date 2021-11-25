import requests
from tok import tok_ya


def _get_headers(tok):
    return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {tok}'
    }


def create_folder(folder_name: str):
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
    headers = _get_headers(tok_ya)
    params = {"path": folder_name}
    response = requests.put(upload_url, headers=headers, params=params)
    return response.status_code


def info(folder_name: str):
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
    headers = _get_headers(tok_ya)
    params = {"path": folder_name}
    response = requests.get(upload_url, headers=headers, params=params)
    return response


def del_folder(folder_name: str):
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
    headers = _get_headers(tok_ya)
    params = {"path": folder_name, 'permanently': True}
    response = requests.delete(upload_url, headers=headers, params=params)
    return response.status_code




