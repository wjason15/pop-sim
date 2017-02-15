from Insect import Insect
import numpy as np
import time


class Sensor:

	locx = 0
	locy = 0
	tcp_port = 0
	tcp_ip = ''
	numOfTypes = 0
	classifier = []
	occurrence = []

	def __init__(self, locx, locy, tcp_port, tcp_ip, numOfTypes):
		self.locx = locx
		self.locy = locy
		self.tcp_port = tcp_port
		self.tcp_ip = tcp_ip
		self.numOfTypes = numOfTypes;
		self.instantiateClassifier()

	def instantiateClassifier(self):
		for i in xrange(self.numOfTypes):
			self.classifier.append(Insect(i, 0.1*i))

	def detect(self):
		self.occurrence = [0] * self.numOfTypes
		for i in xrange(self.numOfTypes):
			lam = self.classifier[i].poissonDist
			self.occurrence[i] = (np.random.poisson(lam, 1))[0]
		return self.occurrence


x = Sensor(0, 0, 100, 'localhost', 10)

while (0):
	sim = x.detect()
	print sim
	time.sleep(3)
