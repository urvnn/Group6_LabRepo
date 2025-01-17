import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Tests for equality based on the student's name."""
        return self.name == other.name

    def __lt__(self, other):
        """Tests if this student's name is less than the other's."""
        return self.name < other.name

    def __ge__(self, other):
        """Tests if this student's name is greater than or equal to the other's."""
        return self.name >= other.name


def main():
    """A simple test for shuffling and sorting a list of Student objects."""
    # Create a list of Student objects with different names
    students = [
        Student("Escobar", 3),
        Student("Buboy", 3),
        Student("Zach", 3),
        Student("Anna", 3),
        Student("Charlie", 3)
    ]

    # Assign scores to each student
    for student in students:
        for i in range(1, 4):
            student.setScore(i, random.randint(50, 100))  # Random scores between 50 and 100

    print("Original list of students:")
    for student in students:
        print(student)
        print()

    # Shuffle the list
    random.shuffle(students)
    print("Shuffled list of students:")
    for student in students:
        print(student)
        print()

    # Sort the list
    students.sort()
    print("Sorted list of students (by name):")
    for student in students:
        print(student)
        print()


if __name__ == "__main__":
    main()
