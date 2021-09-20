'''
https://www.hackerrank.com/challenges/30-class-vs-instance

Write a Person class with an instance variable, age, and a constructor
that takes an integer, initialAge, as a parameter. The constructor must
assign initialAge to age after confirming the argument passed as initialAge
is not negative; if a negative argument is passed as initialAge, the constructor
should set age to 0 and print "Age is not valid, setting age to 0.".

In addition, you must write the following instance methods:
1. yearPasses() should increase the age instance variable by 1.
2. amIOld() should perform the following conditional actions:
    2.1. If age < 13".
    2.2. If age >= 13 and age < 18, print "You are a teenager.".
    2.3. Otherwise, print "You are old.".
'''


class Person:
    age = 0

    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge >= 0:
            self.age = initialAge
        else:
            print('Age is not valid, setting age to 0.')
            self.age = 0

    def am_i_old(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def year_passes(self):
        # Increment the age of the person in here
        self.age += 1


if __name__ == '__main__':
    person = Person(12)
    person.am_i_old()
    person.year_passes()
    person.am_i_old()
    person.year_passes()
    person.year_passes()
    person.year_passes()
    person.year_passes()
    person.year_passes()
    person.am_i_old()
