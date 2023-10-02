from qbittorrent import Client
from dotenv import load_dotenv
import os
import time
load_dotenv()

while True:
    print('Checking for torrents to remove')
    try:
        qb = Client(os.getenv('QB_URL'))
        qb.login(os.getenv('QB_USER'), os.getenv('QB_PASS'))
        torrents = qb.torrents()

        for torrent in torrents:
            print(torrent)
            if torrent['category'] == 'autobrr' and torrent['state'] == 'pausedUP':
                print('Deleting ' + torrent['name'])
                qb.delete_permanently(torrent['hash'])
    except:
        print('Error connecting to qBittorrent')

    time.sleep(300)