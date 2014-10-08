from .copyThread import CopyThread

###
 # @class CopyEngine
 # @brief Main engine of app. Copies file according to provided strategies and file trees
 ###
class CopyEngine:

	def __init__(self, listener, strategy):
		self.__listener = listener
		self.__strategy = strategy # Strategy to apply (e.g.: most recent)			
		self.__threads = 0 # How many threads have been created

	###
	 # Finds provided node in list, using its name
	 ###
	def __findNode(self, srcNode, nodes):
		for n in nodes:
			if n.getContent().getName() == srcNode.getContent().getName():
				return n
		return None

	###
	 # Browses file tree recursively
	 ###
	def __browse(self, srcPath, srcNode, destPath, destNode):
		srcChildren = srcNode.getChildren()
		destChildren = destNode.getChildren()

		for n in srcChildren:
			name = n.getContent().getName()
			outcome = self.__findNode(n, destChildren)

			if outcome is None:
				# Node does not exist, copy file or folder
				CopyThread(self.__listener, srcPath + name, destPath + name, n.getContent().isFolder()).start()
				self.__threads += 1
			else:
				if n.getContent().isFolder():
					# Existing folder, call function again
					self.__browse(srcPath + name + '/', n, destPath + name + '/', outcome)
				else:
					if self.__strategy(n.getContent(), outcome.getContent()):
						# Copy only if strategy is matched
						CopyThread(self.__listener, srcPath + name, destPath + name, False).start()
						self.__threads += 1


	###
	 # Runs engine
	 ###
	def run(self, srcPath, srcTree, destPath, destTree):
		if destTree.isEmpty():
			try:
				shutil.copytree(srcPath, destPath)
			except Exception as e:
				self.__listener.onCopyError(e)
		else:
			self.__browse(srcPath + '/', srcTree.getRoot(), destPath + '/', destTree.getRoot())

		return self.__threads