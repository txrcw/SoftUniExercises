class Flower:
    def __init__(self, name: str, water_requirements: int, is_happy: bool = False):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = is_happy

    def water(self, quantity: int):
        if quantity >= self.water_requirements:
            self.is_happy = True
        return None

    def status(self):
        return f"{self.name} is {'not ' if not self.is_happy else ''}happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
