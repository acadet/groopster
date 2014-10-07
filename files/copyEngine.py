from .copyThread import CopyThread

class CopyEngine:

	def __init__(self, listener, strategy):
		self.__listener = listener	
		self.__strategy = strategy			
		self.__threads = 0

	def __findNode(self, srcNode, nodes):
		for n in nodes:
			if n.getContent().getName() == srcNode.getContent().getName():
				return n
		return None

	def __browse(self, srcPath, srcNode, destPath, destNode):
		srcChildren = srcNode.getChildren()
		destChildren = destNode.getChildren()

		for n in srcChildren:
			name = n.getContent().getName()
			outcome = self.__findNode(n, destChildren)
			if outcome is None:
				CopyThread(self.__listener, srcPath + name, destPath + name, n.getContent().isFolder()).start()
				self.__threads += 1
			else:
				if n.getContent().isFolder():
					self.__browse(srcPath + name + '/', n, destPath + name + '/', outcome)
				else:
					if self.__strategy(n.getContent(), outcome.getContent()):
						CopyThread(self.__listener, srcPath + name, destPath + name, False).start()
						self.__threads += 1


	def run(self, srcPath, srcTree, destPath, destTree):
		if destTree.isEmpty():
			try:
				shutil.copytree(srcPath, destPath)
			except Exception as e:
				self.__listener.onCopyError(e)
		else:
			self.__browse(srcPath + '/', srcTree.getRoot(), destPath + '/', destTree.getRoot())
		return self.__threads