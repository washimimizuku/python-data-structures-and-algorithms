from abc import ABCMeta, abstractmethod

'''
https://www.hackerrank.com/challenges/30-abstract-classes

Given a Book class and a Solution class, write a MyBook class that does the following:

1. Inherits from Book
2. Has a parameterized constructor taking these 3 parameters:
    2.1. string title
    2.2. string author
    2.3. int price
3. Implements the Book class' abstract display() method so it prints these 3 lines:
    3.1. Title:, a space, and then the current instance's title.
    3.2. Author:, a space, and then the current instance's author.
    3.3. Price:, a space, and then the current instance's price.

Note: Because these classes are being written in the same file, you must not use an
access modifier (e.g.: public) when declaring MyBook or your code will not execute.
'''


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass


class MyBook():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = int(price)

    @abstractmethod
    def display(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', self.price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
