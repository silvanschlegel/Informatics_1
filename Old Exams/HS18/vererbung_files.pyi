from abc import ABC,abstractmethod
class FileSystemItem(ABC):
    @abstractmethod
    def size(self):
        pass

class File(FileSystemItem):
    def __init__(self, size):
        self.__size = size
    def size(self):
        return self.__size

class Folder(FileSystemItem):
    def __init__(self, lst):
        self.__items = lst

    def size(self):
        size = 0
        for i in self.__items:
            size += i.size()
        return size

assert File(1).size() == 1
assert Folder([]).size() == 0



