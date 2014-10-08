from window import Window
from files.fileTree import FileTree
from files.copyEngine import CopyEngine
from threading import Lock

###
 # @class Boot
 # @brief Boot class. Builds window and handles process
 ###
class Boot:
    def __init__(self):
        self.__threads = 0
        self.__lock = Lock()

    def start(self):
        self.__window = Window(self)
        self.__window.build()

        self.__window.mainloop()

    ###
     # Run when copying thread has encountered an error
     ###
    def onCopyError(self, error):
        self.__window.showError(error)

    ###
     # Run when copying thread has ended
     ###
    def onCopyEnd(self):
        with self.__lock:
            self.__threads -= 1
            if self.__threads is 0:
                # No more thread, copying engine has ended
                self.__window.showSuccess()

    ###
     # Called when user has launched system
     ###
    def onRun(self, srcDir, targetDir, method):
        # First: build file trees
        originalTree = FileTree(srcDir)
        targetTree = FileTree(targetDir)

        originalTree.build()
        targetTree.build()

        # Now, launch copying engine
        if method is '0':
            copyEngine = CopyEngine(self, lambda x, y: True)
        else:
            copyEngine = CopyEngine(self, lambda x,y: x.getLatestEdition() > y.getLatestEdition())

        outcome = copyEngine.run(srcDir, originalTree, targetDir, targetTree)

        with self.__lock:
            self.__threads += outcome
            if self.__threads is 0:
                # Copy engine has ended after copying threads, process is over
                self.__window.showSuccess()


if __name__ == '__main__':
    Boot().start()