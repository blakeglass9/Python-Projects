# Parent class
class Organism:
    def __init__(self, name="Unknown", species="Unknown", legs=None, arms=None, dna="Sequence A", origin="Unknown", carbon_based=True):
        self.name = name
        self.species = species
        self.legs = legs
        self.arms = arms
        self.dna = dna
        self.origin = origin
        self.carbon_based = carbon_based

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(
            self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg

# Child class Human
class Human(Organism):
    def __init__(self):
        super().__init__(name='MacGuyver', species='Homosapien', legs=2, arms=2, origin='Earth')

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

# Child class Dog
class Dog(Organism):
    def __init__(self):
        super().__init__(name='Spot', species='Canine', legs=4, arms=0, dna='Sequence 5', origin='Earth')

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on its target!"
        return msg

# Child class Bacterium
class Bacterium(Organism):
    def __init__(self):
        super().__init__(name='X', species='Bacteria', legs=0, arms=0, dna='Sequence C', origin='Mars')

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two separate organisms!"
        return msg

# Main block to test the classes
if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacterium = Bacterium()
    print(bacterium.information())
    print(bacterium.replication())
