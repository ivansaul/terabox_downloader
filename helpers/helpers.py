import sys
import time
import requests
from pprint import pprint
from typing import Any, Dict, List

class CustomError(Exception):
    pass


def get_info(short_url: str, pwd: str) -> Dict[Any, Any]:
    url = 'https://terabox-dl.qtcloud.workers.dev/api/get-info'

    params = {
        'shorturl': short_url,
        'pwd': pwd
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    max_retries = 5  # Maximum number of attempts

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()

            data = response.json()
            if (data['ok'] == False):
                raise CustomError(data['message'])
            
            # pprint(data)
            return data

        except requests.exceptions.RequestException as e:
            print(f'Error making API request (attempt {attempt}/{max_retries})')
        
        except CustomError as e:
            print(f'{e} (attempt {attempt}/{max_retries})')
        
        if attempt < max_retries:
            time.sleep(2)
                
        else:
            print('Max retries reached. Giving up.')
            return None


def get_download(short_url: str, pwd: str, shareid: str, uk: str, sign: str, timestamp: str, fs_id: str) -> str:
    url = 'https://terabox-dl.qtcloud.workers.dev/api/get-download'

    body = {
        'shareid': shareid,
        'uk': uk,
        'sign': sign,
        'timestamp': timestamp,
        'fs_id': fs_id,
    }
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    max_retries = 5  # Maximum number of attempts

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(url, json=body, headers=headers)
            response.raise_for_status()

            data = response.json()
            if data['ok'] == False:
                raise CustomError(data['message'])
            
            # pprint(data)
            return data['downloadLink']

        except requests.exceptions.RequestException as e:
            print(f'Error making API request (attempt {attempt}/{max_retries})')

        except CustomError as e:
            print(f'{e} (attempt {attempt}/{max_retries})')

        if attempt < max_retries:
            time.sleep(2)
        else:
            print('Max retries reached. Giving up.')
            return None
        

def getInfoItems(info: Dict[Any, Any]) -> Dict[str, List]:
    data = []
    def getItemRecursive(item: Dict[Any, Any], file_path = '', folder_path = ''):
        if(item['is_dir'] == '1' or item['is_dir'] == 1):
            folder_path = folder_path + '/' + item['filename']
            for item in item['children']:
                getItemRecursive(item, file_path, folder_path)
        else:
            file_path = folder_path + '/' + item['filename']
            # print(file_path)
            data.append({'fs_id': item['fs_id'], 'file_name': item['filename'], 'dir_name': folder_path, 'file_path': file_path})
    
    for item in info['list']:
        getItemRecursive(item)
    
    return {'items': data}


def get_short_url(url: str) -> str:
    return url.strip().split('/')[-1]