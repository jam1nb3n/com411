class Robot:

    # A class attribute
    laws = "Protect, Obey and Survive"

    # A static method
    @staticmethod
    def the_laws():
        print(Robot.laws)

    # a class method
    @classmethod
    def assemble(cls):
        return cls("Assembled Robot")

    # An initialiser (special instance method)
    def __init__(self, name="Robot"):

        # An instance attribute
        self.name = name
        self.age = 0

    # An instance method
    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"robot(name={self.name}, age={self.age})"

    def __str__(self):
        return f"Robot {self.name} is {self.age} years old."
