# Define a metaclass
class NamingConventionMeta(type):
    # This method runs when a class is created
    def __new__(cls, name, bases, class_dict):
        # Check if the class name starts with an uppercase letter
        if not name[0].isupper():
            raise ValueError(f"Class name '{name}' must start with an uppercase letter.")
        # If the check passes, create the class as usual
        return super().__new__(cls, name, bases, class_dict)

# Use the metaclass when creating a new class
class MyClass(metaclass=NamingConventionMeta):
    def greet(self):
        print("Hello from MyClass!")

# Create an object and call a method
obj = MyClass()
obj.greet()        

# Uncommenting the following class will raise an error
# because its name doesn't start with an uppercase letter

class invalidClass(metaclass=NamingConventionMeta):
    pass


