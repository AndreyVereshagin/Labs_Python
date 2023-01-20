from Tableware import Tableware

class Pot(Tableware):
    def __init__(self, D: int, H: int, brand: str, sharpness: bool, size: str, material: str):
        self.D = D
        self.H = H
        self.isContainer = True
        self.name = "Pot"
        super().__init__(brand, sharpness, size, material, self.isContainer, self.name)

    def Volume(self):
        return f'{self.name}: Volume: {self.H*3,14*self.D*self.D/4}'