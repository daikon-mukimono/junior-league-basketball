
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
	for player in inner_players:
		if player["experience"] == "NO":
			player["experience"] = False
		else:
			player["experience"] = True	

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
	print("Select an option:\n1)BALANCE TEAMS\n2)DISPLAY STATS\n3)QUIT\n")

def run_application():
	print("*****WELCOME TO THE KIDS' BASKETBALL LEAGUE TEAM BALANCER*****\n\n")
	display_menu()
	exit_loop = 0

def balance_team():
	pass

def display_stats():
	pass

	while(exit_loop == 0):
		try:
			selection = int(input(">"))

			if selection != 1 and selection != 2 and selection != 3:
				raise ValueError

		except ValueError:
			print("Please select one of the available options!\n")
			display_menu()	

		else:
			exit_loop = 1
			if selection == 1:
				balance_team()

			if selection == 2:
				display_stats()

			if selection == 3:
				print("Goodbye!")	


if __name__ == "__main__":
	prep_data()
	run_application()

