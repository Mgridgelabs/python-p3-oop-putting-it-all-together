#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"  # Default condition when a shoe is created

    @property
    def size(self):
        """The size of the shoe"""
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of the shoe"""
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    def cobble(self):
        """Repairs the shoe and sets its condition to 'New'"""
        print("Your shoe is as good as new!")
        self.condition = "New"