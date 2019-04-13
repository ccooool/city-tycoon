import random 

class Building:

	def __init__(self, building_name):
		# how much money a building makes in revenue per turn
		self.revenue = random.randint(100000,500000)
		self.building_name = building_name
		# the valuation of a building is 10x the revenue 
		self.value = 5 * self.revenue

	def building_details(self):
		return ("the building_name is " + self.building_name + 
			"\n The amount of revenue it produces per turn is " + str(self.revenue))
