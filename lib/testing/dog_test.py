#!/usr/bin/env python3

from dog import Dog

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

def test_is_class():
    '''is a class with the name "Dog"'''
    fido = Dog("Fido")
    assert isinstance(fido, Dog)




