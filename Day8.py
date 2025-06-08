# Define the Car class
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand, model, year, color):
        self.brand = brand      # Brand of the car (e.g., HONDA)
        self.model = model      # Model name (e.g., CITY)
        self.year = year        # Manufacturing year
        self.color = color      # Color of the car

    # Method to display car information
    def display_info(self):
        print(f"\nYour Car Details:")
        print(f"{self.year} {self.color} {self.brand} {self.model}")

# Take user input
brand = input("Enter car brand: ")
model = input("Enter car model: ")
year = input("Enter manufacturing year: ")
color = input("Enter car color: ")

# Create a Car object with user-provided values
my_car = Car(brand, model, year, color)

# Call the display method to show details
my_car.display_info()
