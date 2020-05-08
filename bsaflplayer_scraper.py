#!/bin/python3
#blago
#5/8/20

import requests
import os
from bs4 import BeautifulSoup
from csv import writer, reader
from players_afl import Team, Player
import pandas as pd
from glob import glob

#SET THE FILE path
path = '/Users/blakeedmond/Desktop/PythonCourse/AFLv2_simulator'
os.chdir(f'{path}/team_lists')

teams_urls = {
    'Adelaide Crows': 'https://www.afc.com.au/teams/afl',
    'Brisbane Lions': 'https://www.lions.com.au/teams/afl',
    'Carlton Blues': 'https://www.carltonfc.com.au/teams/afl',
    'Collingwood Magpies': 'https://www.collingwoodfc.com.au/teams/afl',
    'Essendon Bombers': 'https://www.essendonfc.com.au/teams/afl',
    'Fremantle Dockers': 'https://www.fremantlefc.com.au/teams/afl',
    'Geelong Cats': 'https://www.geelongcats.com.au/teams/afl',
    'Gold Coast Suns': 'https://www.goldcoastfc.com.au/teams/afl',
    'Greater Western Sydney Giants': 'https://www.gwsgiants.com.au/teams/afl',
    'Hawthorn Hawks': 'https://www.hawthornfc.com.au/teams/afl',
    'Melbourne Demons': 'https://www.melbournefc.com.au/teams/afl',
    'North Melbourne Kangaroos': 'https://www.nmfc.com.au/teams/afl/players',
    'Port Adelaide Power': 'https://www.portadelaidefc.com.au/teams/afl',
    'Richmond Tigers': 'https://www.richmondfc.com.au/football/afl/squad',
    'St. Kilda Saints': 'https://www.saints.com.au/teams/mens',
    'Sydney Swans': 'https://www.sydneyswans.com.au/teams/afl',
    'West Coast Eagles': 'https://www.westcoasteagles.com.au/football/afl/players',
    'Western Bulldogs': 'https://www.westernbulldogs.com.au/teams/afl',
}

#GENERATE CSV FILES for each AFL team, including: last name, team, position
for team, url in teams_urls.items():
    filename = team
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    player_stats = soup.find_all(class_='squad-list__item')

    with open(f'{filename}.csv', 'a') as csv_file:
        csv_writer = writer(csv_file)
        for player in player_stats:
            name_data = player.find(class_='player-item__name').get_text()
            split_data = name_data.split()
            first = split_data[0]
            last = split_data[1]
            position = split_data[2]
            csv_writer.writerow([first, last, team, position])

#CONCATENATE ALL TEAM_LISTS into one afl_list CSV file: merge_csv(all_files, 'combined_files.csv')
all_files = [i for i in glob('*.csv')]
def merge_csv(all_files, merged_file):
    combined_files = pd.concat([pd.read_csv(f, header=None) for f in all_files], axis=0)
    combined_files.to_csv(f'{path}/{merged_file}', header=None, index=False, encoding='utf-8-sig')

#GENERATE PLAYER/TEAM lists from data contatined in combined_files.csv
os.chdir(path)
club_names = []
player_names = []
with open('combined_files.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        if row not in player_names:
            player_names.append(row)
        else:
            continue
        if row[2] not in club_names:
            club_names.append(row[2])
        else:
            continue

#GENERATE PLAYER/TEAM objects from data contained in combined_files.csv
for club in club_names:
    Team(club)

for player in player_names:
    Player(player)

# #DRAFT PLAYER OBJECTS into their respective team objects
for team in Team.instances:
    for player in Player.undrafted:
        if player.team == team.name:
            team.draft_player(player)
        else:
            pass
