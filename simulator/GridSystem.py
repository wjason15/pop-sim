from Grid import Grid
from random import randint
from Insect import Insect
import time

class GridSystem:
	grids = []
	insects = []
	gridDimension = 0
	numOfTypes = 0

	def __init__(self, gridDimension, numOfTypes):
		self.gridDimension = gridDimension
		self.numOfTypes = numOfTypes
		self.instantiateGrids()
		self.instantiateInsects()

	def instantiateGrids(self):
		self.grids = []
		for i in xrange(self.gridDimension):
			row = []
			for j in xrange(self.gridDimension):
				g = Grid(i, j, self.numOfTypes)
				row.append(g)
			self.grids.append(row)

	def instantiateInsects(self):
		for i in xrange(1000):
			insType = randint(0, self.numOfTypes-1)
			poissonDist = 0.1 * randint(0, 9)
			insX = randint(0, self.gridDimension-1)
			insY = randint(0, self.gridDimension-1)
			self.insects.append(Insect(insType, poissonDist, insX, insY))

	def update(self):
		for i in xrange(self.gridDimension):
			for j in xrange(self.gridDimension):
				self.grids[i][j].reset()
		for insect in self.insects:
			insect.move()
			if (insect.locx >= 0 and insect.locx < self.gridDimension and
				insect.locy >= 0 and insect.locy < self.gridDimension): 
				self.grids[insect.locx][insect.locy].species[insect.insType] += 1

	def showGrids(self):
		for i in xrange(self.gridDimension):
			for j in xrange(self.gridDimension):
				print self.grids[i][j].species,
			print


z = GridSystem(5, 5)
while(0):
	z.update()
	z.showGrids()
	print 
	time.sleep(5)