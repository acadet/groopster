class Tree:

	def __init__(self, root):
		self.__root = root

	def getRoot(self):
		return self.__root

	def isEmpty(self):
		return self.__root is None