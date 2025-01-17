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
    """A simple test"""
    student1 = Student("Escobar", 3)
    student2 = Student("Buboy", 3)

    for i in range(1, 4):
        student1.setScore(i, i * 10)
        student2.setScore(i, i * 20)

    print(f"Student 1: {student1}")
    print(f"Student 2: {student2}")
    print("\nComparisons:")
    print(f"{student1.getName()} == {student2.getName()}? {student1 == student2}")
    print(f"{student1.getName()} < {student2.getName()}? {student1 < student2}")
    print(f"{student1.getName()} >= {student2.getName()}? {student1 >= student2}")


if __name__ == "__main__":
    main()