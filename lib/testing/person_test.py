#!/usr/bin/env python3

from person import Person

class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking.")

def test_is_class():
    '''is a class with the name "Person"'''
    guido = Person("Guido")
    assert isinstance(guido, Person)

class TestInit:
    '''Person.__init__ in person.py'''

    def test_saves_self_name(self):
        '''takes a name as an argument and saves it to self.name'''
        guido = Person("Guido")
        assert(guido.name == "Guido")
