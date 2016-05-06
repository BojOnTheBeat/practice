

class product:
	def __init__(self, name, price, ID, qty):
		self.name = name
		self.price = price
		self.ID = ID
		self.qty = qty




class inventory:
	"""docstring for ClassName"""
	def __init__(self,):
		self.prodList = []

	def sum_inv_value():
		total = 0
		for product in self.prodList:
			total += product.price
		return total


		