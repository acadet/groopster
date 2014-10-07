from window import Window
from files.fileTree import FileTree
from files.copyEngine import CopyEngine
from threading import Lock

class Boot:
    def __init__(self):
        self.__threads = 0
        self.__lock = Lock()

    def start(self):
        self.__window = Window(self)
        self.__window.build()

        self.__window.mainloop()

    def onCopyError(self, error):
        self.__window.showError(error)

    def onCopyEnd(self):
        with self.__lock:
            self.__threads -= 1
            if self.__threads is 0:
                self.__window.showSuccess()

    def onRun(self, srcDir, targetDir, method):
        originalTree = FileTree(srcDir)
        targetTree = FileTree(targetDir)

        originalTree.build()
        targetTree.build()

        if method is '0':
            copyEngine = CopyEngine(self, lambda x, y: True)
        else:
            copyEngine = CopyEngine(self, lambda x,y: x.getLatestEdition() > y.getLatestEdition())

        self.__threads += copyEngine.run(srcDir, originalTree, targetDir, targetTree)

        with self.__lock:
            if self.__threads is 0:
                self.__window.showSuccess()


if __name__ == '__main__':
    Boot().start()