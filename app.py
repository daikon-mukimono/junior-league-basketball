
from constants import TEAMS
from constants import PLAYERS


def clean_height():
	for player in PLAYERS:
		player["height"] = int(player["height"].split(" ")[0])

def clean_exp():
	for player in PLAYERS:
		if player["experience"] == "NO":
			player["experience"] = False
		else:
			player["experience"] = True	

def clean_guardians():
	for player in PLAYERS:
		player["guardians"] = player["guardians"].split(" and ")
		print(player["guardians"])

if __name__ == "__main__":
	clean_height()  	# convert height to an int
	clean_exp()			# convert experience to bool
	clean_guardians()
	#print(PLAYERS)