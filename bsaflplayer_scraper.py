#!/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8
#blago
#5/6/20

import requests
from bs4 import BeautifulSoup
from csv import writer

urls = [
    'https://www.afc.com.au/teams/afl',
    'https://www.lions.com.au/teams/afl',
    'https://www.carltonfc.com.au/teams/afl',
    'https://www.collingwoodfc.com.au/teams/afl',
    'https://www.essendonfc.com.au/teams/afl',
    'https://www.fremantlefc.com.au/teams/afl',
    'https://www.geelongcats.com.au/teams/afl',
    'https://www.goldcoastfc.com.au/teams/afl',
    'https://www.gwsgiants.com.au/teams/afl',
    'https://www.hawthornfc.com.au/teams/afl',
    'https://www.melbournefc.com.au/teams/afl',
    'https://www.nmfc.com.au/teams/afl',
    'https://www.portadelaidefc.com.au/teams/afl',
    'https://www.richmondfc.com.au/football/afl/squad',
    'https://www.saints.com.au/teams/mens',
    'https://www.sydneyswans.com.au/teams/afl',
    'https://www.westcoasteagles.com.au/football/afl/players',
    'https://www.westernbulldogs.com.au/teams/afl'
]

for url in urls:
    filename = url.split('.')[1]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    player_stats = soup.find_all(class_='squad-list__item')

    with open(f'{filename}.csv', 'w') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(['LAST NAME', 'POSITION'])
        for player in player_stats:
            # first = player.find(class_='player-item__name').get_text()
            last = player.find(class_='player-item__last-name').get_text()
            position = player.find(class_='player-item__position').get_text()
            csv_writer.writerow([last, position])

