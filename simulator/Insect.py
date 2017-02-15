import numpy as np
import time

class Insect:
	
	moveRange = [-3,-2,-1,0,1,2,3]
	moveProb = [0.05,0.1,0.2,0.3,0.2,0.1,0.05]

	def __init__(self, insType, poissonDist, locx=0, locy=0, grid=None):
		self.insType = insType
		self.poissonDist = poissonDist
		self.locx = locx
		self.locy = locy
		self.locx = locx
		self.locy = locy
		self.grid = grid

	# probability of destination area is based on distance
	def move(self):
		xdir = np.random.choice(self.moveRange, p=self.moveProb)
		ydir = np.random.choice(self.moveRange, p=self.moveProb)
		#print xdir, ydir
		self.locx += xdir
		self.locy += ydir
		
y = Insect(0, 1)
while (0):
	y.move()
	print y.locx, y.locy
	print 
	time.sleep(3)
