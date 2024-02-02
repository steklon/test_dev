import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
HREF_FOLDER_1 = os.getenv('HREF_FOLDER_1')
HREF_FOLDER_2 = os.getenv('HREF_FOLDER_2')


class TestYandexDiskAPI:

    @pytest.fixture
    def auth_headers(self):
        return {
            'Authorization': f'OAuth {TOKEN}'
        }

    @pytest.mark.parametrize("folder_path, "
                             "expected_status, "
                             "expected_href, "
                             "expected_method, "
                             "expected_templated,"
                             "url",
                             [('/TestFolder1',
                               201,
                               f'{HREF_FOLDER_1}',
                               'GET',
                               False,
                               'https://cloud-api.yandex.net/v1/disk/resources'),
                              ('/TestFolder2',
                               201,
                               f'{HREF_FOLDER_2}',
                               'GET',
                               False,
                               'https://cloud-api.yandex.net/v1/disk/resources'),
                              ('/TestFolder1',
                               409,
                               'Specified path "/TestFolder1" points to existent directory.',
                               'DiskPathPointsToExistentDirectoryError',
                               'По указанному пути "/TestFolder1" уже существует папка с таким '
                               'именем.',
                               'https://cloud-api.yandex.net/v1/disk/resources'),
                              ('/TestFolder',
                               404,
                               'Not Found',
                               'NotFoundError',
                               'Ресурс не найден.',
                               'https://cloud-api.yandex.net/v1/disk/resources1')])
    def test_create_folder(self,
                           auth_headers,
                           folder_path,
                           expected_status,
                           expected_href,
                           expected_method,
                           expected_templated,
                           url):

        headers = auth_headers

        params = {
            'path': folder_path
        }

        response = requests.put(url, headers=headers, params=params)

        assert response.status_code == expected_status

        if expected_status == 201:
            assert response.json()['href'] == expected_href
            assert response.json()['method'] == expected_method
            assert response.json()['templated'] == expected_templated
        else:
            assert response.json()['description'] == expected_href
            assert response.json()['error'] == expected_method
            assert response.json()['message'] == expected_templated

    @pytest.mark.parametrize('folder_path, '
                             'url, '
                             'expected_status',
                             [('/TestFolder1',
                               'https://cloud-api.yandex.net/v1/disk/resources',
                               204),
                              ('/TestFolder2',
                               'https://cloud-api.yandex.net/v1/disk/resources',
                               204)])
    def test_delete_folder(self, auth_headers, folder_path, url, expected_status):

        headers = auth_headers

        params = {
            'path': folder_path,
            'permanently': True
        }

        response = requests.delete(url, headers=headers, params=params)

        assert response.status_code == expected_status

    def test_not_authorized(self):

        url = 'https://cloud-api.yandex.net/v1/disk/resources'

        token = 'INVALID_TOKEN'

        headers = {
            'Authorization': f'OAuth {token}'
        }

        params = {
            'path': '/TestFolder'
        }

        response = requests.put(url, headers=headers, params=params)

        assert response.status_code == 401
