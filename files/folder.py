from .entry import Entry

###
 # @class Folder
 # @brief Represents a folder in a file system
 ###
class Folder(Entry):

	def __init__(self, name):
		Entry.__init__(self, name, True)