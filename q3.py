def wordCount(t):
    # Dictionary to store word occurrences with corresponding line numbers
    word_occurrences = {}

    # Open the file and iterate through each line
    with open(t, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            # Split the line into words
            words = line.split()
            # Iterate through each word in the line
            for word in words:
                # Remove punctuation marks from the word and convert it to lowercase
                word = word.strip('.,!?;:').lower()
                # If the word is not already in the dictionary, add it
                if word not in word_occurrences:
                    word_occurrences[word] = []
                # Append the line number to the list of occurrences for the word
                word_occurrences[word].append(line_num)

    return word_occurrences

word_count = wordCount("words.txt")
print(word_count)
