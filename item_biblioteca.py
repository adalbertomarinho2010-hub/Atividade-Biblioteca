from abc import ABC, abstractmethod

class itembiblioteca(ABC):
    def __init__(self, titulo):
        self._titulo = titulo
        
    @property
    def titulo(self):
        return self._titulo
    
    @abstractmethod
    def tipo(self):
        pass