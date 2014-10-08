from threading import Thread
import random
import time
from threading import Lock

###
 # @class FactDisplayer
 # @brief Displays loaded facts as a thread
 ###
class FactDisplayer(Thread):

	def __init__(self, facts, label):
		Thread.__init__(self)

		self.__facts = facts
		self.__label = label
		self.__canRun = True
		self.__lock = Lock()

	def run(self):
		with self.__lock:
			if not self.__canRun:
				self.__canRun = True
		# Display facts until notification
		while self.__canRun:
			i = random.randint(0, len(self.__facts) - 1)
			self.__label.config(text = self.__facts[i])
			time.sleep(5)

	def stop(self):
		with self.__lock:
			self.__canRun = False
