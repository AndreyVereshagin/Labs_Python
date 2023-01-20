from Tableware import Tableware

class Fork(Tableware):
    def __init__(self, brand: str, sharpness: bool, size: str, material: str):
        self.isContainer = False
        self.name = "Fork"
        super().__init__(brand, sharpness, size, material, self.isContainer, self.name)

    def Volume(self):
        return f"{self.name}: Don't have volume"