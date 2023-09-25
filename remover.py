from qbittorrent import Client
from dotenv import load_dotenv
import os
import time
load_dotenv()

while True:
    print('Checking for torrents to remove')
    qb = Client(os.getenv('QB_URL'))
    qb.login(os.getenv('QB_USER'), os.getenv('QB_PASS'))
    torrents = qb.torrents()

    for torrent in torrents:
        if torrent['category'] == 'autobrr' and torrent['state'] == 'pausedUP':
            print('Deleting ' + torrent['name'])
            qb.delete_permanently(torrent['hash'])

    time.sleep(3600)