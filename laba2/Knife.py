from Tableware import Tableware

class Knife(Tableware):
    def __init__(self, brand: str, sharpness: bool, size: str, material: str):
        self.isContainer = False
        self.name = "Knife"
        super().__init__(brand, sharpness, size, material, self.isContainer, self.name)

    def Volume(self):
        return f"{self.name}: Don't have volume"