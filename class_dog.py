# Define dog here
from class_animal import *

class Dog(Animal):

    def __init__(self, name, legs, owner, dog_collar_shape = 'circle'):
        super().__init__(name, legs)
        self.owner = owner

    def make_sound(self):
        return 'Woof! Woof!'
    def eat_bone(self):
        return 'Yum Yum'
    def run(self):
        return 'Super out of breath now!'
    def greet_owner(self):
        return 'Woof! Hey! Woof!'
