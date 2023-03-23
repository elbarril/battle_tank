from abc import ABC, abstractmethod
#This one or Position class should be an inmutable interface
class MapElement(ABC):
    @property
    @abstractmethod
    def column(self) -> int:
        pass
    
    @column.setter
    @abstractmethod
    def column(self, column) -> None:
        pass

    @property
    @abstractmethod
    def row(self) -> int:
        pass
    
    @row.setter
    @abstractmethod
    def row(self, row) -> None:
        pass
    
    @property
    @abstractmethod
    def is_solid(self) -> bool:
        pass
    
    @is_solid.setter
    @abstractmethod
    def is_solid(self, is_solid) -> None:
        pass