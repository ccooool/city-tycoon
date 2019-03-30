from __future__ import print_function
import sys
import time

class Player(object):


	def __init__(self):
		self.name = ""

	def player_start(self, game):
		print("HI! This is City Tycoon made by Carter Lack :) Hope you enjoy!")
		self.join_game(game)
		self.start_game(game)


	def join_game(self, game):
		while True:
			print("i got here at least")
			new_player = raw_input("What is your name: ").strip()
			print("im received the name")
			self.name = new_player
			print("i set the name to the new player")
			# the server is doing this part!!!
			game.register_player(self.name)
			print("i registered the name")
			break

	def start_game(self, game):
		print("Hi! Welcome to the game! Enter a command!")
		while True:
			response = raw_input("Type a command: ").strip()
			if (response == "how much money do i have?"):
				print(game.get_account_value(self.name))
			if (response == "who else is playing?"):
				print(game.expose_players())




