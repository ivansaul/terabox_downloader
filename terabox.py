from utils.utils import *
from helpers.helpers import *

if __name__ == '__main__':
    
    # FILE "file 0-1.txt"
    # url = 'https://terabox.app/s/1VYMdjlhHyTBnwXaZbuuFTA'

    # FOLDER "a"
    # url = 'https://terabox.app/s/1gOYJQisdSasix_6_TjeJ2A'
   
    # FOLDERS "folder 1" "folder 2"
    # url = 'https://terabox.app/s/1gw0-4rjjtDd6czxCA7aqOA'

    # url = input('Enter TeraBox share link: ')
    short_url = get_short_url(url)
    pwd = ''

    info = get_info(short_url=short_url, pwd=pwd)
    items = getInfoItems(info = info) 

    write_json(info, 'info.json')
    write_json(items, 'items.json')

    shareid = info['shareid']
    uk = info['uk']
    sign = info['sign']
    timestamp = info['timestamp']

    check_path('downloads')

    i, j = 1, len(items['items'])

    for item in items['items']:
        fs_id = item['fs_id']
        file_name = item['file_name']
        file_path = item['file_path']
        download_dir = 'downloads' + item['dir_name']
        download_path = 'downloads' + file_path
        temp_path = download_path + '.aria2'

        # remove temp aria2 file if exists
        if(path_exists(temp_path)):
            remove_file(temp_path)
            remove_file(download_path)

        if(path_exists(download_path)):
            print(f'[{i}/{j}][exists] {file_name}')
            i += 1
        else:
            dl_url = get_download(short_url=short_url, pwd=pwd, shareid=shareid, uk=uk, sign=sign, timestamp=timestamp, fs_id=fs_id)
            check_path(download_dir)
            download(dl_url, download_dir)
            print(f'[{i}/{j}][downloaded] {file_name}')
            i += 1
