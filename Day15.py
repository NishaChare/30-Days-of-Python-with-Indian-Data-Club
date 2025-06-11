import time  # to measure time

# A simple decorator to check how long a function takes to run
def timer_decorator(my_function):
    def wrapper():
        start = time.time()  # start the clock
        my_function()  # run the original function
        end = time.time()  # stop the clock
        print("Time taken:", end - start, "seconds")
    return wrapper  # return the new function

# Use the decorator on your function
@timer_decorator
def say_hello():
    time.sleep(1)  # pretend this takes some time
    print("Hello! I am Nisha")

# Call the function
say_hello()
