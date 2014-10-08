###
 # @class Entry
 # @brief Represents an entry in a file system
 ###
class Entry:

	def __init__(self, name, isFolder):
		self.__name = name;
		self.__isFolder = isFolder

	def getName(self):
		return self.__name

	def isFolder(self):
		return self.__isFolder
