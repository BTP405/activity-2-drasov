import matplotlib.pyplot as plt

def graphSnowfall(t): # Define a function 'graphSnowfall' which takes a file 
    snowfall_ranges = { # Initialize a dictionairy snowfall_ranges, each key represents a range of snowfall, each value is initially set to 0
        '0-10': 0,
        '11-20': 0,
        '21-30': 0,
        '31-40': 0,
        '41-50': 0
    }
    # Opening the file in read mode 
    with open(t, 'r') as file:
        # Looping over each line in the file
        for line in file:
            snowfall = int(line.strip()) # Converting snowfall data from string to integer
            # Iterating over predefined snowfall ranges
            for lower, upper in [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50)]:
                # Check if snowfall value falls within the current range
                if lower < snowfall <= upper:
                    key = f'{lower}-{upper}'
                    snowfall_ranges[key] += 1

    for key, value in snowfall_ranges.items():
        print(f"{value} between {key}cms")

    ranges = list(snowfall_ranges.keys())
    counts = list(snowfall_ranges.values())

    plt.bar(ranges, counts)
    plt.xlabel('Snowfall Ranges (cms)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Distribution')
    plt.savefig("Snowfall.png")
    plt.show()  # Display the plot

# Corrected call to the function
graphSnowfall("Snowfall.txt")
