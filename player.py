from building import Building

class Player():
	def __init__(self):
		self.buildings = []
		self.money = 8000
		self.cost_of_building = 2000

	def buy_new_building(self, building_name):
		if self.money >= self.cost_of_building:
			new_building = Building(building_name)
			self.buildings.append(new_building)
			self.money -= self.cost_of_building
			return new_building.building_details()
		return False

	def get_money(self):
		return self.money

