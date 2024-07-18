class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack!')

class Clown:
    def quack(self):
        print('Quack!')

def make_the_duck_quack(duck: Duck):
    duck.quack()

def make_the_bird_quack(bird: Bird):
    bird.quack()