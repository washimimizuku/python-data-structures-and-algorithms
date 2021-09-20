'''
https://www.hackerrank.com/challenges/30-inheritance

You are given two classes, Person and Student, where Person is the base class
and Student is the derived class. Completed code for Person and a declaration
for Student are provided for you in the editor. Observe that Student inherits
all the properties of Person.

Complete the Student class by writing the following:
1. A Student class constructor, which has  parameters:
1.1. A string, firstName.
1.2. A string, lastName.
1.3. An integer, idNumber.
1.4. An integer array (or vector) of test scores, scores.
2. A char calculate() method that calculates a Student object's average and
   returns the grade character representative of their calculated average:

| Letter |   Average(a)   |
---------------------------
|   O    | 90 <= a <= 100 |
|   E    | 80 <= a <= 90  |
|   A    | 70 <= a <= 80  |
|   P    | 55 <= a <= 70  |
|   D    | 40 <= a <= 55  |
|   T    |       a <= 40  |
---------------------------

Sample Input:

Heraldo Memelli 8135627
2
100 80

Sample Output:

Name: Memelli, Heraldo
ID: 8135627
Grade: O
'''


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        averageScore = 0
        for score in self.scores:
            averageScore += score
        averageScore = int(averageScore/len(self.scores))

        if averageScore >= 90 and averageScore <= 100:
            return 'O'
        elif averageScore >= 80 and averageScore < 90:
            return 'E'
        elif averageScore >= 70 and averageScore < 80:
            return 'A'
        elif averageScore >= 55 and averageScore < 70:
            return 'P'
        elif averageScore >= 40 and averageScore < 55:
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
