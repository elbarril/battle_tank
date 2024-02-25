from abc import ABC, abstractmethod

class Collection(ABC):
    def __init__(self, max_items=None):
        self.__collection = []
        self.__max_items = max_items

    @abstractmethod
    def add(self, object):
        if self.__max_items and len(self) == self.__max_items:
            return Exception(f"Max items {object} exceeded in {self}.")
        self.__collection.append(object)
    
    def __setitem__(self, index, object):
        self.__collection[index] = object
    
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