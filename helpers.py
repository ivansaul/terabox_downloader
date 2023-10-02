import time
import requests
from pprint import pprint

class CustomError(Exception):
    pass


def get_info(short_url, pwd):
    url = 'https://terabox-dl.qtcloud.workers.dev/api/get-info'

    params = {
        'shorturl': short_url,
        'pwd': pwd
    }

    max_retries = 5  # Maximum number of attempts

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            if data['ok'] is False:
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
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    max_retries = 5  # Maximum number of attempts

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(url, json=body, headers=headers)
            response.raise_for_status()

            data = response.json()
            if data['ok'] is False:
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