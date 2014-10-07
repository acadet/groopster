class Node:
	
	def __init__(self, content):
		self.__content = content
		self.__children = []

	def isLeaf(self):
		return len(self.__children) is 0

	def getContent(self):
		return self.__content

	def getChildren(self):
		return self.__children

	def addChild(self, node):
		self.__children.append(node)