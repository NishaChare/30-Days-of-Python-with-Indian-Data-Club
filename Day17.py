# Define our context manager class
class SafeFileHandler:
    """Custom context manager for safe file handling operations."""
    
    def __init__(self, filename, mode='r'):
        """Initialize with filename and access mode."""
        self.filename = filename  # Store the filename
        self.mode = mode          # Store the access mode (read/write/etc)
        self.file = None          # Placeholder for file object
    
    def __enter__(self):
        """Enter the runtime context - open the file."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)  # Open the file
        return self.file  # Return the file object to use in 'with' block
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the runtime context - safely close the file."""
        print(f"Closing file: {self.filename}")
        self.file.close()  # Ensure file is closed
        
        # Handle exceptions if they occurred in the 'with' block
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        # Return True if we handled the exception, False to propagate it
        return True  # Prevents exceptions from propagating

# Example usage
if __name__ == "__main__":
    # Using our context manager to read a file
    try:
        with SafeFileHandler("10numbers.txt", "r") as file:  # Change to a valid file path
            # Read and display the first 5 lines
            print("File content preview:")
            for i, line in enumerate(file):
                if i < 5:  # Show first 5 lines
                    print(line.strip())
                else:
                    break
            # Uncomment to see error handling:
            # raise ValueError("Simulated error during file operations!")
    except Exception as e:
        print(f"Outer error handling: {e}")
    else:
        print("File operation completed successfully!")