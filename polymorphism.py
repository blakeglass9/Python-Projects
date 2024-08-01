# Parent class
class Animal:
    def __init__(self, name, species):
        # Initialize parent class attributes
        self.name = name
        self.species = species

    def make_sound(self):
        # Method to be overridden in child classes
        return "Some generic animal sound"

# Child class Dog inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed, age):
        # Call the parent class __init__ method
        super().__init__(name, species='Canine')
        # Initialize Dog-specific attributes
        self.breed = breed
        self.age = age

    def make_sound(self):
        # Override the parent class method
        return "Woof!"

    def fetch(self):
        # Dog-specific method
        return f"{self.name} is fetching the ball."

# Child class Cat inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color, is_indoor):
        # Call the parent class __init__ method
        super().__init__(name, species='Feline')
        # Initialize Cat-specific attributes
        self.color = color
        self.is_indoor = is_indoor

    def make_sound(self):
        # Override the parent class method
        return "Meow!"

    def purr(self):
        # Cat-specific method
        return f"{self.name} is purring."

# Testing the classes
if __name__ == "__main__":
    # Create an instance of Dog
    my_dog = Dog(name="Buddy", breed="Golden Retriever", age=5)
    print(f"{my_dog.name} the {my_dog.breed} says: {my_dog.make_sound()}")
    print(my_dog.fetch())

    # Create an instance of Cat
    my_cat = Cat(name="Whiskers", color="Black", is_indoor=True)
    print(f"{my_cat.name} the {my_cat.color} cat says: {my_cat.make_sound()}")
    print(my_cat.purr())
