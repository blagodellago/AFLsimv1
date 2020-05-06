#!/bin/python3
#blago
#5/6/20

import requests
from bs4 import BeautifulSoup
from csv import writer
from pathlib import Path

urls = {
    'https://www.afc.com.au/teams/afl': 'Adelaide Crows',
    'https://www.lions.com.au/teams/afl': 'Brisbane Lions',
    'https://www.carltonfc.com.au/teams/afl': 'Carlton Blues',
    'https://www.collingwoodfc.com.au/teams/afl': 'Collingwood Magpies',
    'https://www.essendonfc.com.au/teams/afl': 'Essendon Bombers',
    'https://www.fremantlefc.com.au/teams/afl': 'Fremantle Dockers',
    'https://www.geelongcats.com.au/teams/afl': 'Geelong Cats',
    'https://www.goldcoastfc.com.au/teams/afl': 'Gold Coast Suns',
    'https://www.gwsgiants.com.au/teams/afl': 'Greater Western Sydney Giants',
    'https://www.hawthornfc.com.au/teams/afl': 'Hawthorn Hawks',
    'https://www.melbournefc.com.au/teams/afl': 'Melbourne Demons',
    'https://www.nmfc.com.au/teams/afl/players': 'North Melbourne Kangaroos',
    'https://www.portadelaidefc.com.au/teams/afl': 'Port Adelaide Power',
    'https://www.richmondfc.com.au/football/afl/squad': 'Richmond Tigers',
    'https://www.saints.com.au/teams/mens': 'St. Kilda Saints',
    'https://www.sydneyswans.com.au/teams/afl': 'Sydney Swans',
    'https://www.westcoasteagles.com.au/football/afl/players': 'West Coast Eagles',
    'https://www.westernbulldogs.com.au/teams/afl': 'Western Bulldogs'
}

for url,team in urls.items():
    filename = team
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    player_stats = soup.find_all(class_='squad-list__item')

    path = Path('/Users/blakeedmond/Desktop/PythonCourse/AFLv2_simulator/team_lists')
    with open(f'{path}/{filename}.csv', 'w') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(['LAST NAME', 'TEAM', 'POSITION'])
        for player in player_stats:
            last = player.find(class_='player-item__last-name').get_text()
            position = player.find(class_='player-item__position').get_text()
            csv_writer.writerow([last, team, position])

