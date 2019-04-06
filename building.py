import random 

class Building:

	def __init__(self, building_name):
		self.revenue = random.randint(2000,5000)
		self.building_name = building_name

	def building_details(self):
		return ("the building_name is " + self.building_name + 
			"\n The amount of revenue it produces per turn is " + str(self.revenue))
