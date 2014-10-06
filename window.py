from tkinter import *
from tkinter.filedialog import askdirectory

class Window(Tk):

	def __init__(self, listener):
		Tk.__init__(self)
		self.__listener = listener;

	def build(self):
		self.title('Groopster')

		self.__srcDir = StringVar()
		self.__srcDir.set('Dossier source')
		self.__srcEntry = Entry(self, state = 'readonly', textvariable=self.__srcDir)
		self.__srcEntry.pack()

		self.__srcButton = Button(self, text='Selectionner un dossier', command=self.onSourceButtonClick)
		#self.__srcButton.grid(row = 0, column = 1)
		self.__srcButton.pack()

		self.__targetDir = StringVar()
		self.__targetDir.set('Dossier cible')
		self.__targetEntry = Entry(self, state = 'readonly', textvariable=self.__targetDir)
		self.__targetEntry.pack()

		self.__targetButton = Button(self, text='Selectionner un dossier', command=self.onTargetButtonClick)
		self.__targetButton.pack()

		self.__runButton = Button(self, text='C\'est parti', command=self.onRunButtonClick)
		self.__runButton.pack()

	def onSourceButtonClick(self):
		self.__srcDir.set(askdirectory())

	def onTargetButtonClick(self):
		self.__targetDir.set(askdirectory())

	def onRunButtonClick(self):
		# Test entries
		self.__listener.onRun(self.__srcDir.get(), self.__targetDir.get())
