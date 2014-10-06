from .entry import Entry

class File(Entry):

	def __init__(self, name):
		Entry.__init__(self, name, False)

	def getLatestEdition(self):
		return self.__latestEdition

	def setLatestEdition(self, value):
		self.__latestEdition = value