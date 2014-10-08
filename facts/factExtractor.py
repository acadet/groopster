from threading import Thread

###
 # @class FactExtractor
 # @brief Extracts facts as a thread
 ###
class FactExtractor(Thread):
	def __init__(self, listener):
		Thread.__init__(self)

		self.__listener = listener

	def run(self):
		outcome = []

		with open('assets/random-facts.txt', 'r') as f:
			for line in f:
				outcome.append(line)

		self.__listener.onFactExtractorEnd(outcome)