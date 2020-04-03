from random import shuffle, choice, randint

class Game:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def __repr__(self):
        return f"{self.home_team} vs. {self.away_team}"

    def play_game(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team




class Team:
    def __init__(self):
        teams = [
            "Adelaide",
            "Brisbane",
            "Carlton",
            "Collingwood",
            "Essendon",
            "Fremantle",
            "Geelong",
            "Gold Coast",
            "Greater Western Sydney",
            "Hawthorn",
            "Melbourne",
            "North Melbourne",
            "Port Adelaide",
            "Richmond",
            "St. Kilda",
            "Sydney",
            "West Coast",
            "Western Bulldogs"
        ]

        # for team in teams:
        #     team = Team()
        
        # self.team = team
        i = 0
        while i >= len(teams):
            i += 1
            teams[i] = Team()

    def __repr__(self):
        return teams

class Home_Team(Team):
    def __init__(self):
        super().__init__()

class Away_Team(Team):
    def __init__(self):
        super().__init__()


print(Team())




        # self.away_team = shuffle(Team(teams)).pop(self.team_name)
        # self.vs_team = choice(self.vs_team)

# dictteams = {i : teams[i] for i in range(len(teams))}

# for key in dictteams.keys():
# 	key += 1



# def random_matchups():
# 	while True:
# 		game = {random.shuffle(teams) : random.shuffle(teams)}
# 		for home_team,away_team in game.items():
# 			print(home_team,away_team)
# 		home_team != away_team
# def aflround(roundnumber):
# 	for roundnumber in range(0,23):
# 		random.shuffle(teams)
# 		roundoffooty = [
# 			[teams[0], [teams[1]],
# 			[teams[2], [teams[3],
# 			[teams[4], [teams[5],
# 			[teams[6], [teams[7],
# 			[teams[8], [teams[9],
# 			[teams[10], [teams[11],
# 			[teams[12], [teams[13],
# 			[teams[14], [teams[15],
# 			[teams[16], [teams[17],
# 		]		





# 		# team_scores = {team : random.randint(60,120) for team in teams}
# 		# if score in team_scores.values()  

# 		# for score in team_scores.values():
# 		# 	if team_scores.values() > team_scores.values():
# 		# 		print("home_team wins")
# 		# 	else:
# 		# 		"this is done"

			

# 		# home_team[range(len(home_team))] == random.randint(60,120)
# 		# away_team[range(len(away_team))] == random.randint(60,120)
	
# 		# round_games += 1

		
	
# # print(aflround(0))


# print(random_matchups())

# wins = 0
# losses = 0
# draws = 0 

# # print(dictteams)

# # ***Define below section as 'round'***
# num_playing = 2
# round_games = 0

# while round_games < 9:
# 	list_random_teams = random.choice(teams)
# 	game1 = list_random_teams[0] and list_random_teams[1]
# 	home_team = list_random_teams[0]
# 	away_team = list_random_teams[1]
# 	home_team_score = random.randint(60,120)
# 	away_team_score = random.randint(60,120)

# 	if home_team_score > away_team_score:
# 		print(str(home_team_score) + " " + str(away_team_score) + ": " + home_team + " WINS AGAINST " + away_team)
# 	elif home_team_score < away_team_score:
# 		print(str(home_team_score) + " " + str(away_team_score) + ": " + home_team + " LOSES TO " + away_team)
# 	else:
# 		print(str(home_team_score) + " " + str(away_team_score) + ": " + home_team + " DRAWS WITH " + away_team)
# 	round_games += 1
	

# footy_round = {
# 	"game1" : {home_team : away_team},
# 	"game2" : {home_team : away_team},
# 	"game3" : {home_team : away_team},
# 	"game4" : {home_team : away_team},
# 	"game5" : {home_team : away_team},
# 	"game6" : {home_team : away_team},
# 	"game7" : {home_team : away_team},
# 	"game8" : {home_team : away_team},
# 	"game9" : {home_team : away_team},
# }


		

	
# 	for key,value in dictteams key,value == (random.randint(60,120,1)):
# 		if key > value:
# 			return str(key + " wins")
# 		elif key < value:
# 			return str(key + " wins")
# 		else:
# 			return "Draw"
# print(round_games)
