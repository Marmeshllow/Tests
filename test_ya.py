from ya import create_folder, _get_headers, del_folder
import requests
from tok import tok_ya
import pytest
test_keys_create = [
    ('test3', 201),     # Создано
    ('test1', 409),     # Уже существует
]
test_keys_info = [
    ('test4', 404),     # Не нашли
    ('test1', 200),     # Нашли
]


class TestCreateFolder:

    @pytest.mark.parametrize('folder_name, ex_res', test_keys_create)
    def test_create_folder(self, folder_name, ex_res):
        assert create_folder(folder_name) == ex_res

    @pytest.mark.parametrize('folder_name, ex_res', test_keys_info)
    def test_is_create(self, folder_name, ex_res):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
        headers = _get_headers(tok_ya)
        params = {"path": folder_name}
        response = requests.get(upload_url, headers=headers, params=params)
        assert response.status_code == ex_res

    @classmethod
    def teardown_class(cls):
        for el in test_keys_create:
            del_folder(el[0])



