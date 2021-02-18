#!/bin/python3
#blago
#5/6/20

import requests
import os
from bs4 import BeautifulSoup
from csv import writer, reader
from players_afl import Team, Player
import pandas as pd
import glob

#SET THE FILE path
path = 'C:\\Users\\bedmo\\Programming\\Python_files\\AFLv2_simulator'
os.chdir(f'{path}\\team_lists')

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
            last = player.find(class_='player-item__last-name').get_text()
            position = player.find(class_='player-item__position').get_text()
            csv_writer.writerow([last, team, position])

#CONCATENATE ALL TEAM_LISTS into one afl_list CSV file
all_files = [i for i in glob.glob('*.csv')]
combined_files = pd.concat([pd.read_csv(f) for f in all_files])
combined_files.to_csv(f'{path}/combined_files.csv', index=False, encoding='utf-8-sig')

#GENERATE PLAYER OBJECTS from data contatined in combined_files.csv
os.chdir(path)
club_names = []
with open(f'{path}/combined_files.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        Player(row[0], row[1], row[2])
        if row[1] not in club_names:
            club_names.append(row[1])
        else:
            continue

#GENERATE TEAM OBJECTS from data contained in combined_files.csv
for club in club_names:
    Team(club)

#DRAFT PLAYER OBJECTS into their respective team objects
for team in Team.instances:
    for player in Player.undrafted:
        if player.team == team.name:
            team.draft_player(player)
        else:
            pass
