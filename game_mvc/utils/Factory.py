from abc import ABC, abstractmethod

class Factory(ABC):
    __creations = {}

    @classmethod
    @abstractmethod
    def _create(cls, type, *args):
        type_count = cls.__creations[type] + 1 if type in cls.__creations else 1
        cls.__creations.update({type:type_count})
        return type(*args)
    
    @classmethod
    def _number(cls, type):
        return cls.__creations[type] if type in cls.__creations else 0
    
    @classmethod
    def _next_number(cls, type):
        return cls._number(type) + 1