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
            if torrent['category'] == 'autobrr' and torrent['state'] == 'pausedUP':
                print('Deleting finished torrent: ' + torrent['name'])
                qb.delete_permanently(torrent['hash'])
            elif torrent['category'] == 'autobrr' and torrent['tracker'] == '':
                if torrent['time_active'] > 3600:
                    print('Deleting untracked torrent: ' + torrent['name'])
                    qb.delete_permanently(torrent['hash'])
                else:
                    print('Restarting untracked torrent: ' + torrent['name'])
                    qb.pause(torrent['hash'])
                    qb.resume(torrent['hash'])
            
    except:
        print('Error connecting to qBittorrent')

    time.sleep(300)