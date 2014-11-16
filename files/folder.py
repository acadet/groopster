from .entry import Entry
from .file import File

###
 # @class Folder
 # @brief Represents a folder in a file system
 ###
class Folder(Entry):

    def __init__(self, name):
        Entry.__init__(self, name, True)

    ###
     # Returns files to ignore from any folder
     ###
    @staticmethod
    def filter(folder, fileList):
        ignoredFiles = []
        for f in fileList:
            if File.isIgnored(f):
                ignoredFiles.append(f)

        return ignoredFiles