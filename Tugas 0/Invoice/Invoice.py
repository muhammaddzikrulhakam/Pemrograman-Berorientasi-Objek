class Invoice:
	# Constructor untuk Invoice
	def __init__(self, part_num, part_desc, quantity, price):
		self._part_num = part_num
		self._part_desc = part_desc
		self._quantity = quantity
		if self._quantity < 0:
			self._quantity = 0
		self._price = price
		if self._price < 0:
			self._price = 0

	# Getter dan setter part_num
	@property
	def part_num(self):
		return self._part_num

	@part_num.setter
	def part_num(self, new_part_num):
		self._part_num = new_part_num

	# Getter dan setter untuk part_desc
	@property
	def part_desc(self):
		return self._part_desc

	@part_desc.setter
	def part_desc(self, new_part_desc):
		self._part_desc = new_part_desc

	# Getter dan setter untuk quantity
	@property
	def quantity(self):
		return self._quantity

	@quantity.setter
	def quantity(self, new_quantity):
		self._quantity = new_quantity

	# Getter dan setter untuk price
	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, new_price):
		self._price = new_price

	def get_invoice_amount(self):
		return self._quantity * self._price

