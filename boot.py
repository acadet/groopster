from window import Window
from files.fileTree import FileTree

class Boot:
    def start(self):
        self.__window = Window(self)
        self.__window.build()

        self.__window.mainloop()

    def onRun(self, srcDir, targetDir):
        originalTree = FileTree(srcDir)
        targetTree = FileTree(targetDir)

        originalTree.build()
        targetTree.build()
        print(originalTree)
        print(targetTree)

if __name__ == '__main__':
    Boot().start()