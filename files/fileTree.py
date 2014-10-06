import os
from .file import File
from .folder import Folder
from structs.tree import Tree
from structs.node import Node

class FileTree(Tree):

	def __init__(self, dirName):
		Tree.__init__(self, Node(Folder(dirName)))

	def _buildRec(self, dirNode, path = ''):
		dirName = dirNode.getContent().getName()
		fullPath = path + dirName + '/'
		children = os.listdir(dirName)

		for c in children:
			n = None
			entryPath = fullPath + c
			if os.path.isdir(entryPath):
				n = Node(Folder(c))
				self._buildRec(n, fullPath)
			else:
				f = File(c)
				f.setLatestEdition(os.stat(entryPath).st_mtime)
				n = Node(f)
			dirNode.addChild(n)


	def build(self):
		self._buildRec(self.getRoot())
