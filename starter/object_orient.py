# class Dog:
    # set instance attributes
    # def __init__(self, name, age, breed):
    #     self.name = name
    #     self.age = age
    #     self.breed = breed

    # def description(self):
    #     return f'{self.name} is {self.age} years old'

    # def speak(self, sound):
    #     return f'{self.name} says {sound}'

# create an instance of the Dog class
# my_dog =  Dog('Bingo', 2, 'Shiba')
# your_dog =  Dog('Sept', 3, 'Husky')

# print(my_dog.description())
# print(your_dog.speak('Meow'))

# my_dog.age += 1

# print(my_dog.age, your_dog.age)

######################################################################

#1 
import math
import matplotlib.pyplot as plt
import numpy as np

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 

    # A
    def get_value(self, x):
        return (self.a * x**2) + (self.b * x) + self.c

    # B
    def get_discrim(self):
        return (self.b**2 - (4 * self.a * self.c))

    # C
    def get_zeros(self):
        discrim = self.get_discrim()

        if discrim < 0:
            return None
        
        else:

            pos_root_zero = ((-self.b) + math.sqrt(discrim)) / (2 * self.a)
            neg_root_zero = ((-self.b) - math.sqrt(discrim)) / (2 * self.a)

            return pos_root_zero, neg_root_zero

    # D
    def get_vertex(self):
        vert_x = -(self.b) / (self.a * 2)
        vert_y = self.get_value(vert_x)


        return vert_x, vert_y 

    # E
    def plot_quadratic(self):
        v_x = []

        v_x.append(self.get_vertex())

        x = np.linspace(v_x[0][0] - 10, v_x[0][0] + 10)
        
        y = self.get_value(x)

        plt.plot(x, y)
        
        plt.show()

coefficients = Quadratic(1, 0, 4)

print(coefficients.plot_quadratic())