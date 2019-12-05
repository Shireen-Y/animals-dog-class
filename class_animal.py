# Define animal and methods here

class Animal():
    def __init__(self, name, legs):
        self.bones = True
        self.alive = True
        self.name = name
        self.legs = legs

    def eat(self, food):
        return 'NOM NOM NOM ' + food
    def sleep(self):
        return 'zzzzzz'
    def make_sound(self):
        return 'LaLaLaLa'
