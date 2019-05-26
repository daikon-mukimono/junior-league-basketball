
from constants import TEAMS
from constants import PLAYERS
import copy

###### DATA PREP FUNCTIONS ######
def copy_data():
	global inner_players
	inner_players = copy.deepcopy(PLAYERS)

def clean_height():
	for player in inner_players:
		player["height"] = int(player["height"].split(" ")[0])

def clean_exp():
	global players_with_experience
	global players_no_experience

	players_with_experience =[]
	players_no_experience = []
	for player in inner_players:
		if player["experience"] == "NO":
			player["experience"] = False
			players_no_experience.append(player)
		else:
			player["experience"] = True	
			players_with_experience.append(player)

def clean_guardians():
	for player in inner_players:
		player["guardians"] = player["guardians"].split(" and ")

def prep_data():
	copy_data()
	clean_height()  	# convert height to an int
	clean_exp()			# convert experience to bool
	clean_guardians()	# convert guardians to list		


###### APPLICATION FUNCTIONS ######
def display_menu():
	print("Select an option:\n1)DISPLAY STATS\n2)QUIT\n")

def balance_teams():
	#this function specially created for three-team, 18-kid league
	panthers = []
	bandits = []
	warriors = []

	panthers = players_with_experience[:3] + players_no_experience[:3]
	bandits = players_with_experience[3:6] + players_no_experience[3:6]
	warriors = players_with_experience[6:9] + players_no_experience[6:9]

def select_team():

def display_stats():
	pass

def run_application():
	balance_teams()
	print("*****WELCOME TO THE KIDS' BASKETBALL LEAGUE TEAM BALANCER*****\n\n")
	display_menu()
	exit_loop = 0

	while(exit_loop == 0):
		try:
			selection = int(input(">"))

			if selection != 1 and selection != 2:
				raise ValueError

		except ValueError:
			print("Please select one of the available options!\n")
			display_menu()	

		else:
			exit_loop = 1

			if selection == 1:
				display_stats()

			if selection == 2:
				print("Goodbye!")	


if __name__ == "__main__":
	prep_data()
	run_application()

