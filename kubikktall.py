import numpy as np
import math


try:
    a = int(input('Lower limit: '))                        #Lower limit (integer)
    b = int(input('Upper limit: '))                        #Upper limit (integer)
except ValueError:
    print('Input must be of type integer')
    continue
except TypeError:
    print('Input must be a positive integer')


sum = 0

x = math.floor(a**(1/3))
x_string = str()

while x**3 <= b:
    if x**3 >= a:
        sum = sum + x**3
        x_string = x_string + str(x**3) + (' ')
    x = x + 1

print('Summen er', sum)
print('Tallene er', x_string)