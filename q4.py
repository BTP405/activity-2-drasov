def stats_decorator(func):
    # Define a wrapper function inside hte decorator
    def wrapper(numbers):
        # Print hte numbers read from the file
        print("Numbers read:", numbers)
        # Calculate the count of numbers read
        count = len(numbers)
        # Print hte count of numbers read
        print("Count of numbers read:", count)
        # If there are existing numbers, calculate and print avg, and max
        if count > 0:
            # Calculate the avg of all numbers
            average = sum(numbers) / count
            # Print the average
            print("Average of the numbers:", average)
            # Calculate the max of all numbers
            maximum = max(numbers)
            # Print the max
            print("Maximum of the numbers:", maximum)
            # Seperator for reading clarity
        print("-" * 20)
        # Call the original function printStats with the numbers as arguement
        return func(numbers)
    # Return the wrapper function
    return wrapper

# Decorate printStats function with the stats_decorator
@stats_decorator
def printStats(numbers):
    # This will do nothing because its behavior is defined by the decorator
    pass

# Function to read lines from a file and call the printStats function for eacch line
def read_lines(file_name):
    # Open the file and iterate through each line
    with open(file_name, 'r') as file:
        for line in file:
            # Split the line into individual numbers and convert them to integers
            numbers = [int(num) for num in line.strip().split()]
            # Call the decorated printStats function with the numbers as argument
            printStats(numbers)

# Example usage
read_lines("numbers.txt")
