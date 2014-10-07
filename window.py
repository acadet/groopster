from tkinter import *
from tkinter.filedialog import askdirectory
from facts.factExtractor import FactExtractor
from facts.factDisplayer import FactDisplayer

class Window(Tk):

	def __init__(self, listener):
		Tk.__init__(self)
		self.__listener = listener
		self.__facts = None
		self.__firstTimeFacts = True

		FactExtractor(self).start()

	def __onSourceButtonClick(self):
		self.__srcDir.set(askdirectory())

	def __onTargetButtonClick(self):
		self.__targetDir.set(askdirectory())

	def __onRunButtonClick(self):
		if self.__srcDir.get() == 'Dossier source':
			self.__showPopup('Il me faut un dossier source si cela ne t\'embête pas. A moins que tu aimes le travail inutile...')
		elif self.__targetDir.get() == 'Dossier cible':
			self.__showPopup('Il me faut un dossier cible. Je veux bien te le mettre quelque part au pif, mais tu risques de ne pas apprécier...')
		else:
			self.__runButton.config(text = 'J\'y bosse...', state = 'disabled')
			self.__runFacts()
			self.__listener.onRun(self.__srcDir.get(), self.__targetDir.get(), self.__selectedMethod.get())

	def __runFacts(self):
		if self.__facts is None:
			return

		if self.__firstTimeFacts:
			self.__firstTimeFacts = False
			factFrame = Frame(self)
			factFrame.grid(row = 3, column = 0)
			Label(factFrame, text = 'Un peu de savoir inutile : ').grid(row = 0, column = 0)
			self.__factLabel = Label(factFrame, width = 150)
			self.__factLabel.grid(row = 1, column = 0)

		self.__factThread = FactDisplayer(self.__facts, self.__factLabel)
		self.__factThread.start()

	def __stopFacts(self):
		if self.__factThread:
			self.__factThread.stop()

	def __showPopup(self, msg):
		top = Toplevel()
		top.title('Groopster')

		message = Message(top, text = msg)
		message.pack()

		button = Button(top, text = 'Je te remercie', command = top.destroy)
		button.pack()

	def build(self):
		self.title('Groopster')

		inputFrame = Frame(self)
		inputFrame.grid(row = 0, column = 0)

		self.__srcDir = StringVar()
		self.__srcDir.set('Dossier source')
		srcEntry = Entry(inputFrame, state = 'readonly', textvariable = self.__srcDir, width = 50)
		srcEntry.grid(row = 0, column = 0)

		srcButton = Button(inputFrame, text = 'Sélectionner un dossier', command = self.__onSourceButtonClick)
		srcButton.grid(row = 0, column = 1)

		self.__targetDir = StringVar()
		self.__targetDir.set('Dossier cible')
		targetEntry = Entry(inputFrame, state = 'readonly', textvariable = self.__targetDir, width = 50)
		targetEntry.grid(row = 1, column = 0)

		targetButton = Button(inputFrame, text = 'Sélectionner un dossier', command = self.__onTargetButtonClick)
		targetButton.grid(row = 1, column = 1)

		methodFrame = Frame(self)
		methodFrame.grid(row = 1, column = 0, sticky = 'w')

		methodLabel = Label(methodFrame, text='Méthode à utiliser', justify = 'left')
		methodLabel.grid(row = 0, column = 0, sticky = 'w')

		self.__selectedMethod = StringVar()
		method1 = Radiobutton(methodFrame, text='Remplacer si source plus récente', variable=self.__selectedMethod, value='1', justify = 'left')
		method1.grid(row = 1, column = 0, sticky = 'w')
		method1.select()
		method2 = Radiobutton(methodFrame, text='Remplacer', variable=self.__selectedMethod, value='0', justify = 'left')
		method2.grid(row = 2, column = 0, sticky = 'w')
		method2.deselect()

		self.__runButton = Button(self, text='C\'est parti', command=self.__onRunButtonClick)
		self.__runButton.grid(row = 2, column = 0)	

	def showSuccess(self):
		self.__stopFacts()
		self.__showPopup('Encore du travail bien fait !')
		self.__runButton.config(text = 'Encore une fois ?', state = 'normal')

	def showError(self, error):
		self.__stopFacts()
		self.__showPopup('Aie :( L\'erreur suivante s\'est produite : ' + str(error))

	def onFactExtractorEnd(self, facts):
		self.__facts = facts

