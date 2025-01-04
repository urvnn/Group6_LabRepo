"""
Program: generator_modified.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary. Words are chosen at random.
"""

import random
import os

def accept(filename):
    """Reads words from a file and returns them as a tuple."""
    with open(filename, 'r') as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return tuple(words)

# Define the path to the 'source' folder
sourcefolder = "source"

# Load vocabulary from files in the 'source' folder
articles = accept(os.path.join(sourcefolder, "articles.txt"))
nouns = accept(os.path.join(sourcefolder, "nouns.txt"))
verbs = accept(os.path.join(sourcefolder, "verbs.txt"))
prepositions = accept(os.path.join(sourcefolder, "prepositions.txt"))

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
