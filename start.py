import sys
import Pyro4
import Pyro4.util
from client import Client

game = Pyro4.Proxy("PYRONAME:CityTycoon")
player = Client()
player.player_start(game)