from colorama import Fore, Style
from ClassPlane import Plane

class Airport:
    def __init__(self):
        self.__planes = []
    
    @property
    def planes(self):
        return self.__planes
    @planes.setter
    def addPlane(self, plane):
        self.__planes.append(plane)

    def __str__(self):
        return str(self.planes)
    
    
    