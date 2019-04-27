from building import Building

class Player():
	def __init__(self, turn_num, name):
		self.name = name
		self.buildings = []
		self.money = 800000
		self.cost_of_building = 200000
		self.ready = False
		self.turn_num = turn_num

	def buy_new_building(self, building_name):
		if self.money >= self.cost_of_building:
			new_building = Building(building_name)
			self.buildings.append(new_building)
			self.money -= self.cost_of_building
			return new_building.building_details()
		return False

	def get_money(self):
		return self.money

	def get_name(self):
		return self.name

	def get_num_buildings(self):
		return len(self.buildings)

	def set_ready(self, ready_status):
		self.ready = ready_status

	def is_ready(self):
		return self.ready 

	def get_turn_num(self):
		return self.turn_num

 	def collect_money(self):
 		for building in self.buildings:
 			self.money += building.get_revenue()
 		return self.money

 	def get_building_values(self):
 		buildings_list = []
 		for building in self.buildings:
 			buildings_list.append(("building name: " + building.get_name(), "building value: " + str(building.get_value()), "building revenue: " + str(building.get_revenue()) ))
 		return buildings_list

 	def sell_building(self, building_name):
 		for index, building in enumerate(self.buildings):
 			if (building.get_name() == building_name):
 				self.money += building.get_value()
 				self.buildings.pop(index)
 				return self.money
 		return -1




