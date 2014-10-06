from .entry import Entry

class Folder(Entry):

	def __init__(self, name):
		Entry.__init__(self, name, True)