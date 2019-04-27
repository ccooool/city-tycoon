from __future__ import print_function
import Pyro4
from collections import defaultdict
from player import Player

@Pyro4.expose
@Pyro4.behavior(instance_mode = "single")

class CityTycoonServer(object):

	def __init__(self):
		self.players = defaultdict()
		self.turn_to_player = defaultdict()
		self.turn_num = 0

	@Pyro4.expose
	def register_player(self, name):
		print("im getting here")
		self.players[name] = Player(self.turn_num, name)
		self.turn_to_player[self.turn_num] = name
		self.turn_num += 1


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
		count = 0
		for player_name in self.players.keys():
			count += 1
			if not self.players[player_name].is_ready():
				all_ready = False
		if (count == 1): return False
		return all_ready

	@Pyro4.expose
	def total_turns(self):
		return self.turn_num

	@Pyro4.expose
	def reset_all_players_ready(self):
		for player_name in self.players.keys():
			self.players[player_name].set_ready(False)

	@Pyro4.expose
	def check_player_ready(self, turn_num):
		player_name = self.turn_to_player[turn_num]
		return self.players[player_name].is_ready()

	@Pyro4.expose
	def get_player(self, turn_num):
		return self.turn_to_player[turn_num]

	@Pyro4.expose
	def collect_money(self, player_name):
		player = self.players[player_name]
		player_money = player.collect_money()
		return player_money


	@Pyro4.expose
	def check_for_winners(self):
		for player_name in self.players.keys():
			player = self.players[player_name]
			if (player.get_money() >= 10000000 or player.get_num_buildings() >= 10):
				print(player.get_money())
				print(player.get_num_buildings())
				return player_name
		return None

	@Pyro4.expose
	def get_building_values(self, name):
		player = self.players[name]	
		return player.get_building_values()

	@Pyro4.expose
	def sell_building(self, player_name, building_name):
		return (self.players[player_name]).sell_building(building_name)

	@Pyro4.expose
	def view_money(self, player_name):
		return (self.players[player_name]).get_money()



	




def main():
	Pyro4.Daemon.serveSimple(
		{
			CityTycoonServer: "CityTycoon"
		},
		ns = True)

if __name__ == "__main__":
	main()
