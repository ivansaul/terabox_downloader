from helpers import *
from pprint import pprint

if __name__ == '__main__':
    
    # FILE
    # short_url = 'https://terabox.com/s/1poJGVNkbufY3l-vS8dmznw'
    short_url = '1poJGVNkbufY3l-vS8dmznw'
    pwd = ''

    # FOLDER
    # short_url = 'https://terabox.com/s/1a7xUpndOxJ7awuMB2cCTYA'
    short_url = '1a7xUpndOxJ7awuMB2cCTYA'
    pwd = ''
    
    shareid='500793992'
    uk='4402319809216'
    sign='2a946ab137d14f069212fde341643bdb08c796ea'
    timestamp='1696217962'
    fs_id='855958613995216'

    info= get_info(short_url=short_url, pwd=pwd)
    dl_url = get_download(short_url=short_url, pwd=pwd, shareid=shareid, uk=uk, sign=sign, timestamp=timestamp, fs_id=fs_id)

    # pprint(info)
    pprint(dl_url)
