from __future__ import print_function
import Pyro4
from collections import defaultdict

@Pyro4.expose
@Pyro4.behavior(instance_mode = "single")

class CityTycoonServer(object):

	def __init__(self):
		self.players = defaultdict()

	@Pyro4.expose
	def register_player(self, name):
		print("im getting here")
		self.players[name] = 5000

	@Pyro4.expose 
	def get_account_value(self, key):
		return self.players[key]

	@Pyro4.expose
	def expose_players(self):
		return self.players.keys()


def main():
	Pyro4.Daemon.serveSimple(
		{
			CityTycoonServer: "CityTycoon"
		},
		ns = True)

if __name__ == "__main__":
	main()
