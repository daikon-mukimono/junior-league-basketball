
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
	global panthers
	global bandits
	global warriors

	panthers = []
	bandits = []
	warriors = []

	panthers = players_with_experience[:3] + players_no_experience[:3]
	bandits = players_with_experience[3:6] + players_no_experience[3:6]
	warriors = players_with_experience[6:9] + players_no_experience[6:9]

def select_team():
	print("Select one of the options below!")
	
	exit_loop = 0
	while(exit_loop == 0):
		try:
			print("1)Panthers Stats\n2)Bandits Stats\n3)Warriors Stats\n4)Return to main menu\n5)Quit program")
			selection = int(input(">"))	

			if selection < 1 or selection > 5:
				raise ValueError
		except ValueError:
			print("try again!")
		else:
			exit_loop = 1

			if selection == 1:
				display_stats(1)
			elif selection == 2:
				display_stats(2)
			elif selection == 3:
				display_stats(3)
			elif selection == 4:
				run_application()
			elif selection == 5:
				print("Goodbye!")	


def display_stats(team):
	if team == 1:
		print("**********************")
		print("******PANTHERS********")
		print("**********************\n\n")
		print("Number of players:" + str(len(panthers)))
		print("Players:")
		new_panthers = []
		for player in panthers:
			new_panthers.append((player["name"]))
		print(", ".join(new_panthers))
		print("Experienced Panthers: " + str(int(len(panthers)/2)))
		print("Inexperienced Panthers: " + str(int(len(panthers)/2)))
		total_height = 0
		for player in panthers:
			total_height += player["height"]
		print("Average Height: " + str(round(total_height/len(panthers),2)) + " inches")

	if team == 2:
		print("**********************")
		print("*******BANDITS********")
		print("**********************\n\n")
		print("Number of players:" + str(len(bandits)))
		print("Players:")
		new_bandits = []
		for player in bandits:
			new_bandits.append((player["name"]))
		print(", ".join(new_bandits))
		print("Experienced Bandits: " + str(int(len(bandits)/2)))
		print("Inexperienced Bandits: " + str(int(len(bandits)/2)))
		total_height = 0
		for player in bandits:
			total_height += player["height"]
		print("Average Height: " + str(round(total_height/len(bandits),2)) + " inches")


	if team == 3:
		print("**********************")
		print("*******WARRIORS*******")
		print("**********************\n\n")
		print("Number of players:" + str(len(warriors)))
		print("Players:")
		new_warriors = []
		for player in warriors:
			new_warriors.append((player["name"]))
		print(", ".join(new_warriors))
		print("Experienced Bandits: " + str(int(len(warriors)/2)))
		print("Inexperienced Bandits: " + str(int(len(warriors)/2)))
		total_height = 0
		for player in warriors:
			total_height += player["height"]
		print("Average Height: " + str(round(total_height/len(warriors),2)) + " inches")		

	print("\n\nDisplaying team menu:\n")
	select_team()	
	

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
				select_team()

			elif selection == 2:
				print("Goodbye!")	


if __name__ == "__main__":
	prep_data()
	run_application()

