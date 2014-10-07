from threading import Thread
import random
import time

class FactDisplayer(Thread):

	def __init__(self, facts, label):
		Thread.__init__(self)

		self.__facts = facts
		self.__label = label

	def run(self):
		self.__canRun = True
		while self.__canRun:
			i = random.randint(0, len(self.__facts) - 1)
			self.__label.config(text = self.__facts[i])
			time.sleep(5)

	def stop(self):
		self.__canRun = False
