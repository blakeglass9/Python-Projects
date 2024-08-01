# Parent class
class Vehicle:
    """
    This is the parent class 'Vehicle' which will be inherited by other classes.
    It has common attributes and methods that will be shared by its child classes.
    """
    def __init__(self, make, model, year):
        """
        Initialize the attributes of the Vehicle class.
        :param make: Manufacturer of the vehicle
        :param model: Model of the vehicle
        :param year: Year of manufacture
        """
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        Display the information about the vehicle.
        """
        return f"{self.year} {self.make} {self.model}"

# Child class 1
class Car(Vehicle):
    """
    This class 'Car' inherits from the 'Vehicle' class.
    It adds additional attributes specific to cars.
    """
    def __init__(self, make, model, year, number_of_doors, is_convertible):
        """
        Initialize the attributes of the Car class.
        :param number_of_doors: Number of doors on the car
        :param is_convertible: Whether the car is convertible or not
        """
        super().__init__(make, model, year)  # Call the parent class constructor
        self.number_of_doors = number_of_doors
        self.is_convertible = is_convertible

    def display_info(self):
        """
        Override the display_info method to include car-specific details.
        """
        basic_info = super().display_info()
        return f"{basic_info}, Doors: {self.number_of_doors}, Convertible: {self.is_convertible}"

# Child class 2
class Truck(Vehicle):
    """
    This class 'Truck' inherits from the 'Vehicle' class.
    It adds additional attributes specific to trucks.
    """
    def __init__(self, make, model, year, cargo_capacity, is_diesel):
        """
        Initialize the attributes of the Truck class.
        :param cargo_capacity: Cargo capacity of the truck in tons
        :param is_diesel: Whether the truck uses diesel fuel or not
        """
        super().__init__(make, model, year)  # Call the parent class constructor
        self.cargo_capacity = cargo_capacity
        self.is_diesel = is_diesel

    def display_info(self):
        """
        Override the display_info method to include truck-specific details.
        """
        basic_info = super().display_info()
        return f"{basic_info}, Cargo Capacity: {self.cargo_capacity} tons, Diesel: {self.is_diesel}"

# Example usage
if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2020, 4, True)
    my_truck = Truck("Ford", "F-150", 2021, 5, True)

    print(my_car.display_info())  # Output the car information
    print(my_truck.display_info())  # Output the truck information
