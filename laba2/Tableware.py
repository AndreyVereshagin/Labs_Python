from abc import ABC, abstractmethod

class Tableware(ABC):
    def __init__(self, brand: str, sharpness: bool, size: str, material: str, isContainer: bool, name: str):
        self.brand = brand
        self.sharpness = sharpness
        self.size = size
        self.material = material
        self.isContainer = isContainer
        self.name = name

    def __repr__(self) -> str:
        if self.isContainer == True:
            return f'<{self.name}: brand: {self.brand}, sharpness: {self.sharpness}, size: {self.size}, material: {self.material} this is the container>'
        else:
            return f'<brand: {self.brand}, sharpness: {self.sharpness}, size: {self.size}, material: {self.material} this is not the container>'

    @abstractmethod
    def Volume(self):
        pass