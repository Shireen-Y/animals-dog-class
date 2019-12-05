# Import stuff here
from class_animal import *
from class_dog import *

animal1 = Animal('Jimmy', 6)
animal2 = Animal('Sandra', 4)

dog1 = Dog('Bob', 4, 'Billy')
dog2 = Dog('Jimbob', 4, 'Craig')

print(animal1.sleep())
print(animal2.eat('yummy leaves!'))
print(dog1.make_sound())
print(dog2.greet_owner())
