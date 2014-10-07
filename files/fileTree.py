import os
from .file import File
from .folder import Folder
from structs.tree import Tree
from structs.node import Node

class FileTree(Tree):

	def __init__(self, dirName):
		Tree.__init__(self, Node(Folder(dirName)))

	def __buildRec(self, dirNode, path = ''):
		dirName = dirNode.getContent().getName()
		fullPath = path + dirName + '/'
		children = os.listdir(fullPath)

		for c in children:
			n = None
			entryPath = fullPath + c
			if os.path.isdir(entryPath):
				n = Node(Folder(c))
				self.__buildRec(n, fullPath)
			else:
				f = File(c)
				stats = os.stat(entryPath)
				f.setLatestEdition(stats.st_mtime)
				# f.setSize(stats.st_size / 1000)
				n = Node(f)
			dirNode.addChild(n)


	def build(self):
		self.__buildRec(self.getRoot())

	def printTree(self):
		def f(node, pre):
			extendedPre = pre + '-'
			for n in node.getChildren():
				print(extendedPre + n.getContent().getName())
				if n.getContent().isFolder():
					f(n, extendedPre)

		if self.isEmpty():
			print('Empty tree')
		else:
			print(self.getRoot().getContent().getName())
			f(self.getRoot(), '')	
