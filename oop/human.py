class Human:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        self.age += 1

    def eat(self, amount):
        i = 0
        while i < amount:
            if self.energy != Human.MAX_ENERGY:
                self.energy += 1
            i += 1

    def move(self, distance):
        i = 0
        while i < distance:
            if self.energy != 0:
                self.energy -= 1
            i += 1

    def __repr__(self):
        return f"human(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"Human {self.name} is {self.age} years old with energy {self.energy}."