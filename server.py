from __future__ import print_function
import Pyro4
from collections import defaultdict
from player import Player

@Pyro4.expose
@Pyro4.behavior(instance_mode = "single")

class CityTycoonServer(object):

	def __init__(self):
		self.players = defaultdict()

	@Pyro4.expose
	def register_player(self, name):
		print("im getting here")
		self.players[name] = Player()

	@Pyro4.expose 
	def get_account_value(self, key):
		return self.players[key].get_money()

	@Pyro4.expose
	def expose_players(self):
		return self.players.keys()

	@Pyro4.expose
	def check_availability(self, name):
		# return true if the name you want is not 
		# in the list of players
		return name not in self.players.keys()

	@Pyro4.expose
	def buy_a_building(self, name, building_name):
		return self.players[name].buy_new_building(building_name)

	@Pyro4.expose
	def signal_ready(self, name):
		self.players[name].set_ready(True)

	@Pyro4.expose
	def players_ready(self):
		all_ready = True
		for player_name in self.players.keys():
			if not self.players[player_name].is_ready():
				all_ready = False
		return all_ready
	




def main():
	Pyro4.Daemon.serveSimple(
		{
			CityTycoonServer: "CityTycoon"
		},
		ns = True)

if __name__ == "__main__":
	main()
