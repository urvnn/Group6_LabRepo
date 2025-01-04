def mode(f):
    
    words = []
    for line in f:
        wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())
    
    theDictionary = {}
    
    for word in words:
        number = theDictionary.get(word, None)
        if number is None:
            theDictionary[word] = 1
        else:
            theDictionary[word] = number + 1

    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            return key

def median(f):
    
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

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