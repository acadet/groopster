from threading import Thread
from .folder import Folder
import shutil

###
 # @class CopyThread
 # @brief Copies file or folder as a thread
 ###
class CopyThread(Thread):

	def __init__(self, listener, src, dest, isTree):
		Thread.__init__(self)

		self.__listener = listener
		self.__src = src
		self.__dest = dest
		self.__isTree = isTree

	def run(self):
		f = None
		if (self.__isTree):
			f = lambda: shutil.copytree(self.__src, self.__dest, False, Folder.filter)
		else:
			f = lambda: shutil.copy(self.__src, self.__dest)

		try:
			f()
		except Exception as e:
			self.__listener.onCopyError(e)
		else:
			self.__listener.onCopyEnd()
