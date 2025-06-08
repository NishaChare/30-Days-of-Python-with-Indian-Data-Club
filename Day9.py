# Parent class: Car
class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year


    def display_info(self):
        print(f"{self.brand} {self.model} {self.color} {self.year}")

# Child class: electricCar (inherits from Car)
class electricCar(Car):
    def __init__(self, brand, model, color, year, battery_capacity):
        # Call the parent class constructor using super()
        super().__init__(brand, model, color, year)
        self.battery_capacity = battery_capacity  # new attribute

    # Method overriding: Polymorphism in action
    def display_info(self):
        print(f"{self.brand} {self.model} {self.color} {self.year} {self.battery_capacity} kWh")
        
# Creating objects
car1 = Car("Honda", "City", "Red" , 2021)
car2 = electricCar("Tesla", "Model 1", "white", 2025, 85)

# Calling methods
car1.display_info()       # Output: Honda City Red 2021
car2.display_info()       # Output: Tesla Model 1 white 2025 85 kWh
