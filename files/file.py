from .entry import Entry

###
 # @class File
 # @brief Represents a file in a file system
 ###
class File(Entry):

	def __init__(self, name):
		Entry.__init__(self, name, False)

	def getLatestEdition(self):
		return self.__latestEdition

	def setLatestEdition(self, value):
		self.__latestEdition = value

	# def getSize(self, value):
	# 	return self.__size

	# def setSize(self, value):
	# 	self.__size = value

	###
	 # Sets if a file has to be ignored
	 ###
	@staticmethod
	def isIgnored(name):
		n = name.lower().strip()
		if n == 'thumbs.db' or n == '.ds_store':
			return True

		return False
