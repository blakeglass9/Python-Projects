from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    # Abstract method (to be implemented by child classes)
    @abstractmethod
    def make_sound(self):
        pass

    # Regular method
    def describe(self):
        return f"This is a {self.name}."

# Child class implementing the abstract method
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Another child class implementing the abstract method
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Utilize both parent and child methods
print(dog.describe())  # From the parent class
print(dog.make_sound())  # Implemented in the child class

print(cat.describe())  # From the parent class
print(cat.make_sound())  # Implemented in the child class
