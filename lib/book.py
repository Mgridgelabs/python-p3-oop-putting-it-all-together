#!/usr/bin/env python3

from turtle import title



class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        """The title of the book"""
        return self._title

    @title.setter
    def title(self, new_title):
        """Sets the title of the book"""
        if isinstance(new_title, str):
            self._title = new_title
        else:
            raise ValueError("Title must be a string.")
        
    @property
    def page_count(self):
        """The number of pages in the book"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, count):
        if isinstance(count, int):
            self._page_count = count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Simulates turning a page in the book"""
        print("Flipping the page...wow, you read fast!")

book = Book("And Then There Were None",272)
print(book.title)
print(book.page_count)