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
		while True:
			# check for the player's input
			self.lobby_menu()

			response = raw_input("Type a command: ").strip()


			# now check the command prompt
			if (response == "start da game" or response == "s"):
				print("the game will commence as soon as all players in the lobby are ready")
				break
			elif (response == "who else is playing?" or response == "p"):
				print(game.expose_players())

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
		print("either buy 10 buildings or get to 10 million dollars first in order to win the game!!")
		while (True):

			game.reset_all_players_ready()

			for i in range(game.total_turns()):
				print("player " + game.get_player(i) + " is taking their turn")
				# wait for each player to finish their turn 
				if game.get_player(i) != self.name:
					print("waiting for " + game.get_player(i) + " to finish their turn")
					while (True):
						if game.check_player_ready(i):
							break

				else: 
					self.game_options(game)
				possible_winner = game.check_for_winners()
				if possible_winner:
					print("Player " + possible_winner + " has won the game!")
					print("Ending the game now. Thanks for playing!!!")
					return
					

	def game_options(self, game):
		print("it's your turn! make a command")
		while (True):
			self.game_menu()
			response = raw_input("Type a command for this turn: ").strip()
			if response == "e" or response == "end turn":
				print("im trying to end my turn")
				break
			elif (response == "buy a building" or response == "b"):
				building_name = raw_input("What kind of building do you want: ").strip()
				building_success = game.buy_a_building(self.name, building_name)
				if (building_success):
					print("success! you bought a building")
					print(building_success)
				else:
					print("not enof money")
				break
		money_collected = game.collect_money(self.name)
		print("At this point you have " + str(money_collected) + " dollars after collecting from your buildings")
		game.signal_ready(self.name)




			


	def lobby_menu(self):
		print("Here is the lobby menu:")
		print("s | start da game")
		print("p | who else is playing?")

	def game_menu(self):
		print("Here is the game menu:")
		print("e | end turn")
		print("b | buy a building")








