from __future__ import print_function
import sys
import time

class Client(object):


	def __init__(self):
		self.name = ""

	def player_start(self, game):
		print("HI! This is City Tycoon made by Carter Lack :) Hope you enjoy!")
		self.join_game(game)
		self.queue_for_game(game)


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

	def queue_for_game(self, game):
		print("Hi! Welcome to the game! Enter a command!")
		self.menu()
		while True:
			# check for the player's input
			response = raw_input("Type a command: ").strip()
			self.menu()

			# now check the command prompt
			if (response == "start da game" or response == "s"):
				print("the game will commence as soon as all players in the lobby are ready")
				break
			elif (response == "how much money do i have?" or response == "m"):
				print(game.get_account_value(self.name))
			elif (response == "who else is playing?" or response == "p"):
				print(game.expose_players())
			elif (response == "buy a building" or response == "b"):
				building_name = raw_input("What kind of building do you want: ").strip()
				building_success = game.buy_a_building(self.name, building_name)
				if (building_success):
					print("success! you bought a building")
					print(building_success)
				else:
					print("not enof money")
			else:
				print("command not found")
		self.wait_for_start(game)

	def wait_for_start(self, game):
		game.signal_ready(self.name)
		# waiting for other players to be ready
		while True:
			# check if the other players are ready
			if game.players_ready():
				print("all players were ready, starting the game!!!")
				self.start_game(game)
				break	

	def start_game(self, game):
		print("started the game successfully!!!!")
			


	def menu(self):
		print("Here is the menu:")
		print("s | start da game")
		print("m | how much money do i have?")
		print("p | who else is playing?")
		print("b | buy a building")






