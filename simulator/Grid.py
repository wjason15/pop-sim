class Grid:

	def __init__(self, locx, locy, numOfTypes):
		self.locx = locx
		self.locy = locy
		self.numOfTypes = numOfTypes
		self.instantiateSpecies()

	def instantiateSpecies(self):
		self.species = []
		for i in xrange(self.numOfTypes):
			self.species.append(0)

	def update(self, insType):
		self.species[insType] += 1

	def reset(self):
		for i in xrange(self.numOfTypes):
			self.species[i] = 0

	def numOfInsects(self):
		res = 0
		for s in self.species:
			res += s
		return res