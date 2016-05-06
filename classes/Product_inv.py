

class product:
	def __init__(self, name, price, ID, qty):
		self.name = name
		self.price = price
		self.ID = ID
		self.qty = qty

	def get_price(self):
		return self.price

	def set_price(self, new_price):
		self.price = new_price

	def get_qty(self):
		return self.qty

	def set_qty(self, new_qty):
		self.qty = new_qty




class inventory:
	"""docstring for inventory class"""
	def __init__(self,):
		self.prodList = []

	def sum_inv_value():
		total = 0
		for product in self.prodList:
			total += product.get_price
		return total

	def add_product(self, product):
		self.prodList.append(product)

	def remove_product(self, prod_ID):
		for product in self.prodList:
			if product.ID is prod_ID:
				self.prodList.remove(product)

	def view_inventory(self):
		return self.prodList
























		