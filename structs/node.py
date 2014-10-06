class Node:
	
	def __init__(self, content):
		self.__content = content
		self.__children = []

	def isLeaf(self):
		return len(self.__children) is 0

	def getContent(self):
		return self.__content

	def forEachChildren(self, func):
		for e in self.__children:
			func(e)

	def addChild(self, node):
		self.__children.append(node)