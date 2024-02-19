from abc import ABC, abstractmethod

class Collection(ABC):
    def __init__(self):
        self.__collection = []

    @abstractmethod
    def add(self, object):
        self.__collection.append(object)
    
    def clear(self):
        self.__collection = []

    def __tuple__(self):
        return tuple(self.__collection)

    def __iter__(self):
        self.__index = 0
        return self

    @abstractmethod
    def __next__(self):
        if self.__index < len(self):
            obj = self[self.__index]
            self.__index += 1
            return obj
        raise StopIteration

    @abstractmethod
    def __getitem__(self, index):
        return self.__collection[index]

    def __len__(self):
        return len(self.__collection)

    def __str__(self):
        return str([str(obj) for obj in self.__collection])