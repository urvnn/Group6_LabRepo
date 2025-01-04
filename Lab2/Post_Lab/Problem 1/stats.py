def mode(f):
    # Input the text, convert its words to uppercase, and
    # add the words to a list
    words = []
    for line in f:
        wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())

    # Obtain the set of unique words and their
    # frequencies, saving these associations in
    # a dictionary
    theDictionary = {}
    
    for word in words:
        number = theDictionary.get(word, None)
        if number is None:
            # word entered for the first time
            theDictionary[word] = 1
        else:
            # word already seen, increment its number
            theDictionary[word] = number + 1

    # Find the mode by obtaining the maximum value
    # in the dictionary and determining its key
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            return key


def median(f):
    # Input the text, convert it to numbers, and
    # add the numbers to a list
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

    # Sort the list and return the number at its midpoint
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2
    
    
def mean(f):
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))
    
    if not numbers:
        return 0
    
    return round((sum(numbers) / len(numbers)), 2)
    
def main():
    fileName = input("Enter the file name: ")
    with open(fileName, 'r') as f:
        print("The mode is", mode(f))
    
    with open(fileName, 'r') as f:
        print("The median is", median(f))
    
    with open(fileName, 'r') as f:
        print("The mean is", mean(f))
    
if __name__ == "__main__":
    main()