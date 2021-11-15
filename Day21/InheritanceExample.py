class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("In general all animals inhale and exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print(f"Fish breathe under water with the help of gills and they have {self.num_of_eyes} eyes")

    @staticmethod
    def swim():
        print("Swims in water")


nemo = Fish()
nemo.breathe()
nemo.swim()
