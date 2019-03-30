import sys
import Pyro4
import Pyro4.util
from client import Player

game = Pyro4.Proxy("PYRONAME:CityTycoon")
player = Player()
player.player_start(game)