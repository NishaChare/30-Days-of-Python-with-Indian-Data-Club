try:
    # Attempt to open the file
    with open("numbers.txt", "r") as file:
        lines = file.readlines()

    # Convert each line to an integer
    numbers = [int(line.strip()) for line in lines]
    print("Numbers read from file:", numbers)

except FileNotFoundError:
    # Handle the case where the file doesn't exist
    print("Error: The file 'numbers.txt' was not found.")

except ValueError:
    # Handle case where conversion to int fails
    print("Error: One or more lines in the file are not valid integers.")

except Exception as e:
    # Catch all other unforeseen errors
    print("An unexpected error occurred:", e)

finally:
    # This block always executes (even if there's an error)
    print("File reading attempt finished.")
