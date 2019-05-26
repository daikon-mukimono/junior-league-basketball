
from constants import TEAMS
from constants import PLAYERS


def get_height():
	for player in PLAYERS:
		player["height"] = player["height"].split(" ")[0]




if __name__ == "__main__":
	print(TEAMS)
	get_height()