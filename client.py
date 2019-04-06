from __future__ import print_function
import sys
import time

class Client(object):


	def __init__(self):
		self.name = ""

	def player_start(self, game):
		print("HI! This is City Tycoon made by Carter Lack :) Hope you enjoy!")
		self.join_game(game)
		self.start_game(game)


	def join_game(self, game):
		while True:
			new_player = raw_input("What is your name: ").strip()
			if (game.check_availability(new_player)):
				self.name = new_player
				# the server is doing this part!!!
				game.register_player(self.name)
				break
			print("no the name is not avalibol")
			print("choose a nother name")

	def start_game(self, game):
		print("Hi! Welcome to the game! Enter a command!")
		self.menu()
		while True:
			print("")
			response = raw_input("Type a command: ").strip()
			print("")
			self.menu()
			print("")
			if (response == "how much money do i have?" or response == "m"):
				print(game.get_account_value(self.name))
			if (response == "who else is playing?" or response == "p"):
				print(game.expose_players())
			if (response == "buy a building" or response == "b"):
				building_name = raw_input("What kind of building do you want: ").strip()
				building_success = game.buy_a_building(self.name, building_name)
				if (building_success):
					print("success! you bought a building")
					print(building_success)
				else:
					print("not enof money")

	def menu(self):
		print("Here is the menu:")
		print("m | how much money do i have?")
		print("p | who else is playing?")
		print("b | buy a building")




